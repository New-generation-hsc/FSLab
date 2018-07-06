"""
This module define the `File` and `Directory` class
And this module define the `File System` 
"""
import datetime
from exception import CmdNotFound, PathException, ArgumentException

class Node(object):
    """
    this is the File and Directory base class
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.create_time = datetime.datetime.now()

        self.permission = {} # the key is username, the value is xwr ---
        self._isdir = None # current file whether is file or directory
        self.subdirectory = None # the sub directory
        self._parent = None 

    @property
    def name(self):
        return self.file_name

    @property
    def time(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def isdir(self):
        return self._isdir

    @isdir.setter
    def isdir(self, dir_or_not):
        self._isdir = dir_or_not

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def permission(self, username):
        val = self.permission.get(username)
        if val:
            return val
        else:
            return 0

    def display(self, deep):
        pass


class File(Node):
    """
    The `File` class define File Node
    """
    def __init__(self, file_name):
        super(File, self).__init__(file_name)
        self.isdir = False
        self.subdirectory = None

    def display(self, deep):
        print('.' * 4 * deep, end='')
        print(self.name)


class Directory(Node):
    """
    The `Directory` class define Directory Node
    """
    def __init__(self, file_name):
        super(Directory, self).__init__(file_name)
        self.isdir = True
        self.subdirectory = []

    def append(self, directory):
        self.subdirectory.append(directory)

    def remove(self, file):
        self.subdirectory.remove(file)

    def display(self, deep):
        print('.' * 4 * deep, end='')
        print(self.name)
        for node in self.subdirectory:
            node.display(deep + 1)


class FileSystem(object):
    """
    the file system is tree based system, and every node has pointer point to the parent node
    """
    def __init__(self):
        super(FileSystem, self).__init__()
        self.cur_path = ['/'] # the current path, that will be show in the console
        self.root = Directory('/') 
        self.cur_dir = self.root # the current directory node

    def create_file(self, file_name):
        """
        in current path, create a new file
        """
        node = File(file_name)
        node.parent = self.cur_dir
        self.cur_dir.append(node)

    def create_directory(self, file_name):
        """
        in current path, create a new directory
        """
        node = Directory(file_name)
        node.parent = self.cur_dir
        self.cur_dir.append(node)

    def search(self, file_name):
        """
        in the current directory, search file or directory
        """
        target = None
        for node in self.cur_dir.subdirectory:
            if node.name == file_name:
                return node
        return target

    def _switch_path(self, file_list):
        if not file_list or len(file_list) == 0:
            return 
        first = file_list[0]
        if first == '.':
            self._switch_path(file_list[1:])
        elif first == '..' and not self.cur_dir.parent:
            self.cur_path = self.cur_path[:len(self.cur_path) - 1]
            self.cur_dir = self.cur_dir.parent
        elif first == '':
            pass
        else:
            node = self.search(first)
            if not node or not node.isdir:
                raise PathException("path not valid")
            self.cur_path.append(node.name)
            self.cur_dir = node
        self._switch_path(file_list[1:])

    def switch(self, path):
        """
        change path
        """
        if path.startswith('/'):
            self.cur_path = ['/']
            self.cur_dir = self.root
            self._switch_path(path.split('/')[1:])
        else:
            self._switch_path(path.split('/'))

    @property
    def files(self):
        """
        return current path files include directory
        """
        return self.cur_dir.subdirectory

    @property
    def path(self):
        """
        return current path
        """
        return ''.join(self.cur_path)

    def delete_file(self, file_path):
        """
        delete file from current path
        """
        current_path = self.path
        path, _, file = file_path.rpartition('/')
        path = '/' if not path else path
        self.switch(path)
        node = self.search(file)
        if node:
            self.cur_dir.remove(node)
        self.switch(current_path)

    def delete_directory(self, dir_path):
        """
        delete directory from current path
        """
        cur_path = self.path
        self.switch(dir_path)
        self._del_dir()
        _, _, dir_name = dir_path.rpartition('/')
        self.switch('..')
        file = self.search(dir_name)
        self.cur_dir.remove(file)
        self.switch(cur_path)

    def _del_dir(self):

        for file in self.cur_dir.subdirectory:
            if not file.isdir:
                self.delete_file(file.name)
            else:
                self.switch(file.name)
                self._del_dir()
                self.switch('..')
        self.cur_dir.subdirectory = []

    def display(self):
        """
        display current directory file name include directory
        """
        self.root.display(0)
        


if __name__ == "__main__":

    fs = FileSystem()
    fs.create_file('fl1')
    fs.create_directory('dir')

    fs.switch('dir')
    fs.create_file('f2')
    fs.create_directory('dir2')
    fs.display()

    fs.switch('/fs2')

    #fs.delete_directory('/dir')
    #fs.display()
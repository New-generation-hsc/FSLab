"""
This module define the user file table and system file table
every user has a user file table
"""
def print_line(length=16, end='\n'):
    print('+', '-' * length, '+', sep='', end=end)


def print_content(content, length=16, char='|', end='\n'):
    """
    print file name in the center of rectangle
    """
    space_len = length - len(content)
    left_len = space_len // 2
    right_len = space_len - left_len
    print(char, ' ' * left_len, content, ' ' * right_len, char, sep='', end=end)


def print_user_line(content_len, user_len):
    print('+', '-' * content_len, '+', '-' * user_len, '+', sep='')


def print_user_content(content, user, content_len, user_len):
    """
    print system file table
    """
    content_space = content_len - len(content)
    content_left = content_space // 2
    content_right = content_space - content_left
    user_space = user_len - len(user)
    user_left = user_space // 2
    user_right = user_space - user_left
    print('|', ' ' * content_left, content, ' ' * content_right, '~', ' ' * user_left, user, ' ' * user_right, '~', sep='')


class UserFileTable:

    def __init__(self, user):
        self.belong = user
        self.file_list = []

    def get_belong(self):
        return self.belong

    def get_file_list(self):
        return self.file_list

    def search_file_u(self, file_route):
        if file_route in self.file_list:
            return file_route
        else:
            return None

        '''
        if file_route in self.file_list:
            return True
        else:
            return False
        '''

    def add_file_u(self, file_route):
        if not self.search_file_u(file_route):
            self.file_list.append(file_route)

        '''
        if not self.search_file(file_route):
            self.file_list.append(file_route)
        '''

    def delete_file_u(self, file_route):
        if self.search_file_u(file_route):
            self.file_list.remove(file_route)

    def display(self):
        """ display a specific user file table in the console """
        if len(self.file_list) == 0:
            return
            
        length = len(max(self.file_list, key=lambda x : len(x)))
        length = 16 if length < 16 else length + 2
        print_line(length)
        print_content(self.belong, length, char='~')
        print_line(length)
        for file in self.file_list:
            print_content(file, length)
            print_line(length)


class SystemFileTable:
    def __init__(self):
        admin_table = UserFileTable('admin')
        guest_table = UserFileTable("guest")
        self.file_table = [admin_table, guest_table]

    def add_user(self, username):
        if not self.search_user_s(username):
            temp = UserFileTable(username)
            self.file_table.append(temp)

    def delete_user(self, username):
        temp = self.search_user_s(username)
        if temp:
            self.file_table.remove(temp)

    def search_user_s(self, user):
        for file_list in self.file_table:
            if file_list.get_belong() == user:
                return file_list
        return None

    def check_user_file(self, user, file_route):
        """
        check a user whether open a specific file
        """
        file_table = self.search_user_s(user)
        if file_table:
            return file_table.search_file_u(file_route)
        return False

    def add_file_s(self, current_user, file_route):
        temp = self.search_user_s(current_user)
        if temp:
            temp.add_file_u(file_route)

    def delete_file_s(self, current_user, file_route):
        temp = self.search_user_s(current_user)
        if temp:
            temp.delete_file_u(file_route)

    def display(self):
        files = [path for table in self.file_table for path in table.file_list]
        if len(files) == 0:
            return
        content_len = len(max(files, key=lambda x: len(x)))
        user_len = len(max([table.belong for table in self.file_table], key=lambda x: len(x)))

        content_len = 16 if content_len < 16 else content_len + 2
        user_len = 16 if user_len < 16 else user_len + 2

        print_user_line(content_len, user_len)
        for table in self.file_table:
            for path in table.file_list:
                print_user_content(path, table.belong, content_len, user_len)
                print_user_line(content_len, user_len)


if __name__ == "__main__":
    file_table = SystemFileTable()
    file_table.display()
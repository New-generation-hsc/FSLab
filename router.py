from command import app
import settings
import surface
import real
import os
from exception import AuthenticationException, FileAccessException



@app.route([], cmd='ls')
def list_path(args):
    """
    list current path files and directory
    """
    fs = settings.System.getInstance().system
    surface.print_files(fs.files)


@app.route(['-f'], cmd='ls')
def list_files(args):
    """
    list the given files
    """
    fs = settings.System.getInstance().system
    files = list(filter(lambda x : not x.isdir, fs.files))
    surface.print_files(files)


@app.route(['-s'], cmd='ls')
def list_sorted_path(args):
    """
    list the current path and display them in order
    """
    fs = settings.System.getInstance().system
    files = sorted(fs.files, key= lambda x : x.name)
    surface.print_files(files)


@app.route(['-d'], cmd='ls')
def list_directory(args):
    """
    list current path directory
    """
    fs = settings.System.getInstance().system
    directories = list(filter(lambda x : x.isdir, fs.files))
    surface.print_files(directories)


@app.route(['-l'], cmd='ls')
def list_information(args):
    """ list files information """
    fs = settings.System.getInstance().system
    surface.print_details(fs.files)


@app.route(['-s', '-d'], cmd='ls')
def list_sorted_directory(args):
    """
    list the current directory in order
    """
    fs = settings.System.getInstance().system
    directories = list(filter(lambda x : x.isdir, fs.files))
    files = sorted(directories, key=lambda x : x.name)
    surface.print_files(files)


@app.route(['-s', '-f'], cmd='ls')
def list_sorted_files(args):
    """
    list the current path files in order
    """
    fs = settings.System.getInstance().system
    files = list(filter(lambda x : not x.isdir, fs.files))
    files = sorted(files, key=lambda x : x.name)
    surface.print_files(files)


@app.route(['-s', '-l'], cmd='ls')
def list_sorted_detail(args):
    """
    list the files detail in order
    """
    fs = settings.System.getInstance().system
    files = sorted(fs.files, key=lambda x : x.name)
    surface.print_details(files)


@app.route([], cmd='cd')
def change_directory(args):
    """
    change the directory
    """
    fs = settings.System.getInstance().system
    fs.switch(args.path)


@app.route([], cmd='mkdir')
def create_directory(args):
    """
    create new directory
    """
    fs = settings.System.getInstance().system
    fat = settings.Singleton.getInstance().fat
    for file_name in args.directory:
        node = fs.create_directory(file_name)
        if node:
            real.create_directory(node.path)
            node.set_size(real.get_size(node.path))
            item = fat.allocate()
            node.set_inode(item.current)
            fat.reallocate(item.current, node.size)


@app.route([], cmd='rm')
def remove_file(args):
    """
    just remove files
    """
    fs = settings.System.getInstance().system
    for file_name in args.path:
        node = fs.delete_file(file_name)
        if node:
            real.delete_file(node.path)
            fat = settings.Singleton.getInstance().fat
            fat.release(node.inode)


@app.route(['-r'], cmd='rm')
def remove_directory(args):
    """
    recursive remove files from directory
    """
    fs = settings.System.getInstance().system
    for file_name in args.path:
        node = fs.delete_directory(file_name)
        if node:
            real.delete_directory(node.path)
            fat = settings.Singleton.getInstance().fat
            fat.release(node.inode)


@app.route([], cmd='touch')
def touch_file(args):
    """
    create a new empty file
    """
    fs = settings.System.getInstance().system
    fat = settings.Singleton.getInstance().fat
    for file_name in args.files:
        node = fs.create_file(file_name)
        if node:
            real.create_file(node.path)
            node.set_size(real.get_size(node.path))
            item = fat.allocate()
            node.set_inode(item.current)
            fat.reallocate(item.current, node.size)


@app.route([], cmd='su')
def switch_to_user(args):
    """
    switch to user
    update current_user
    current_user = args.username
    """
    username = args.username
    password = surface.obtain_pass("password: ")
    manager = settings.Singleton.getInstance().manager
    result = manager.login(username, password)
    if not result:
        raise AuthenticationException("username or password error")


@app.route([], cmd='adduser')
def add_user(args):
    """
    Add new users
    """
    '''raise NotImplementedError("Not Implemented Yet")'''
    username = args.username
    password = surface.obtain_pass("password: ")
    confirm = surface.obtain_pass("password confirm: ")
    if password == confirm:
        manager = settings.Singleton.getInstance().manager
        result = manager.add_user(username, password)
        fs = settings.System.getInstance().system
        if result:
            node = fs.create_user_directory(result)
            table = settings.Singleton.getInstance().table
            table.add_user(result.name)
            if node:
                real.create_directory(node.path)
                node.set_size(real.get_size(node.path))
                fat = settings.Singleton.getInstance().fat
                item = fat.allocate()
                node.set_inode(item.current)
                fat.reallocate(item.current, node.size)
    else:
        raise AuthenticationException("two password are not unanimous")


@app.route([], cmd='deleteuser')
def delete_user(args):
    """
    delete old user
    """
    '''raise NotImplementedError("Not Implemented Yet")'''
    username = args.username
    manager = settings.Singleton.getInstance().manager
    result = manager.delete_user(username)
    if result:
        fs = settings.System.getInstance().system
        node = fs.delete_user_directory(result)
        table = settings.Singleton.getInstance().table
        table.delete_user(result.name)
        if node:
            real.delete_directory(node.path)
            fat = settings.Singleton.getInstance().fat
            fat.release(node.inode)

@app.route([], cmd='checkuser')
def check_user(args):
    """
    check current users
    """
    '''raise NotImplementedError("Not Implemented Yet")'''
    manager = settings.Singleton.getInstance().manager
    manager.display()


@app.route([], cmd='format')
def format(args):
    """
    format contents according to current users
    """
    user = settings.Singleton.getInstance().user
    fs = settings.System.getInstance().system
    if user.name == "admin":
        path = fs.path
        fs.switch('/')
        users = settings.Singleton.getInstance().manager.get_users()
        files = list(filter(lambda x : x.name not in [user.name for user in users], fs.files))
        for file in files:
            if file.isdir:
                real.delete_directory(file.path)
            else:
                real.delete_file(file.path)
        for user in users:
            real.format_user_directory(user)
        fs.format()

@app.route(['-u'], cmd='format')
def format_user(args):
    """
    format a user
    """
    user = settings.Singleton.getInstance().user
    fs = settings.System.getInstance().system
    manager = settings.Singleton.getInstance().manager
    if user.name == "admin":
        user = manager.get_user(args.u)
        if user:
            fs.format(user)
            real.format_user_directory(user)


@app.route([], cmd='clear')
def clear_screen(args):
    """
    there too much content in the screen, clear the screen
    """
    surface.clear_screen()


@app.route([], cmd='read')
def read_file(args):
    """

    :param args:
    :return:
    """

    fs = settings.System.getInstance().system
    file = fs.search(args.file)
    user = settings.Singleton.getInstance().user
    table = settings.Singleton.getInstance().table
    if file and not file.isdir:
        if not table.check_user_file(user.name, file.path):
            raise FileAccessException("file not open", file.path)
        with open(settings.BASE_PATH + file.path, 'r', encoding='utf-8') as f:
            print(f.read())


@app.route([], cmd='write')
def write_file(args):
    """

    """
    fs = settings.System.getInstance().system
    file = fs.search(args.file)
    user = settings.Singleton.getInstance().user
    table = settings.Singleton.getInstance().table
    if file and not file.isdir:
        if not table.check_user_file(user.name, file.path):
            raise FileAccessException("file not open", file.path)
        with open(settings.BASE_PATH + file.path, 'a+', encoding='utf-8') as f:
            f.write(args.content)
        file.set_size(real.get_size(file.path))
        fat = settings.Singleton.getInstance().fat
        print(file.inode, file.size)
        fat.reallocate(file.inode, file.size)


@app.route([], cmd='open')
def open_file(args):
    """
    open a file for write and read
    """
    fs = settings.System.getInstance().system
    file = fs.search(args.file)
    table = settings.Singleton.getInstance().table
    user = settings.Singleton.getInstance().user
    if file:
        table.add_file_s(user.name, file.path)


@app.route([], cmd='close')
def close_file(args):
    """
    close a file
    """
    fs = settings.System.getInstance().system
    file = fs.search(args.file)
    table = settings.Singleton.getInstance().table
    user = settings.Singleton.getInstance().user
    if file:
        table.delete_file_s(user.name, file.path)


@app.route([], cmd='table')
def display_system_table(args):
    """
    close a file
    """
    table = settings.Singleton.getInstance().table
    table.display()

@app.route(['-u'], cmd='table')
def display_user_table(args):
    """
    close a file
    """
    table = settings.Singleton.getInstance().table
    user = settings.Singleton.getInstance().user
    user_table = table.search_user_s(user.name)
    if user_table:
        user_table.display()


@app.route([], cmd='node')
def show_nodes(args):
    fs = settings.System.getInstance().system
    file = fs.search(args.file)
    fat = settings.Singleton.getInstance().fat
    if file:
        fat.display(file.inode)

if __name__ == "__main__":

    app.run('')
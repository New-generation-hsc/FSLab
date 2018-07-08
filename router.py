from command import app
import settings
import surface
from exception import AuthenticationException


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
    files = filter(lambda x : not x.isdir, fs.files)
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
    directories = filter(lambda x : x.isdir, fs.files)
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
    directories = filter(lambda x : x.isdir, fs.files)
    files = sorted(directories, key=lambda x : x.name)
    surface.print_files(files)


@app.route(['-s', '-f'], cmd='ls')
def list_sorted_files(args):
    """
    list the current path files in order
    """
    fs = settings.System.getInstance().system
    files = filter(lambda x : not x.isdir, fs.files)
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
    for file_name in args.directory:
        fs.create_directory(file_name)


@app.route([], cmd='rm')
def remove_file(args):
    """
    just remove files
    """
    fs = settings.System.getInstance().system
    for file_name in args.path:
        fs.delete_file(file_name)


@app.route(['-r'], cmd='rm')
def remove_directory(args):
    """
    recursive remove files from directory
    """
    fs = settings.System.getInstance().system
    for file_name in args.path:
        fs.delete_directory(file_name)


@app.route([], cmd='touch')
def touch_file(args):
    """
    create a new empty file
    """
    fs = settings.System.getInstance().system
    for file_name in args.files:
        fs.create_file(file_name)


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
            fs.create_user_directory(result)
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
        fs.delete_user_directory(result)

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
    raise NotImplementedError("Not Implemented Yet")


@app.route([], cmd='clear')
def clear_screen(args):
    """
    there too much content in the screen, clear the screen
    """
    surface.clear_screen()


if __name__ == "__main__":

    app.run('')
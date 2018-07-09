"""
The module define the UI interface
"""

import settings
import getpass
import os

CMD_COLOR = {
    'HEADER' : '\033[95m',
    'BLUE' : '\033[94m',
    'GREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m',
    'ENDC' : '\033[0m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m'
}


def format_path(path, user):
    if path == '':
        return '/'
    elif path.startswith('/' + user.name):
        return '~' + path[len(user.name) + 1:]
    return path


def print_prompt():
    user = settings.Singleton.getInstance().user
    name = "guest" if not user else user.name
    path = settings.System.getInstance().path
    path = format_path(path, user)
    print(CMD_COLOR['GREEN'] + "({}): ".format(name) + "{}".format(path) + " > " + CMD_COLOR['ENDC'], end='')


def clear_screen():
    """ clear screen according to system version """
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")

def print_file(file):
    """
    print file name in the console no color
    """
    name = file.name
    rest = 15 - len(name)
    print(name + ' ' * rest, end='')


def print_directory(directory):
    """ print directory name in the console with blue color """
    name = directory.name
    rest = 15 - len(name)
    print(CMD_COLOR['BLUE'] + name + CMD_COLOR['ENDC'] + ' ' * rest, end='')


def print_path(file):
    """ print file or directory in the console """
    if file.isdir:
        print_directory(file)
    else:
        print_file(file)


def print_error(msg):
    """ print error msg in the console """
    print(CMD_COLOR['FAIL'] + msg + CMD_COLOR['ENDC'])


def print_files(files):
    """ print files or directory in the console, and five file in one row """
    for count, file in enumerate(files):
        print_path(file)
        if (count + 1) % 5 == 0:
            print()
    if len(list(files)) % 5 > 0:
        print()


def obtain_pass(msg):
    """ get password from console """
    return getpass.getpass(msg)


def calc_permission(permission, shift_val):
    return (permission & 2**shift_val) >> shift_val

def print_file_info(file):
    """ print file detail information in the console """
    access_mode = ['c', 'd', 'w', 'r']
    permission_str = ""
    mode_len = len(access_mode)
    user_permission = file.permission(settings.Singleton.getInstance().user.name)
    for i, mode in enumerate(access_mode):
        permission = calc_permission(user_permission, mode_len - 1 - i)
        permission_str += mode if permission else "-"

    print(permission_str, file.belongs.name, file.time,  end='')
    print(' ' * 2, end='')
    print_path(file)
    print()

def print_details(files):
    for file in files:
        print_file_info(file)
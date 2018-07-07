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


def print_prompt():
	user = settings.Singleton.getInstance().user
	name = "guest" if not user else user.name
	path = settings.System.getInstance().path
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
	rest = 16 - len(name)
	print(name + ' ' * rest, end='')


def print_directory(directory):
	""" print directory name in the console with blue color """
	name = directory.name
	rest = 16 - len(name)
	print(CMD_COLOR['BLUE'] + name + CMD_COLOR['ENDC'], ' ' * rest)


def print_path(file):
	""" print file or directory in the console """
	if file.isdir:
		print_directory(file)
	else:
		print_file(file)


def print_error(msg):
	""" print error msg in the console """
	print(CMD_COLOR['FAIL'] + msg + CMD_COLOR['ENDC'])
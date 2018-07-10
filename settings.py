"""
config the project setting
and construct the global variable
"""
from user_manage import UserManager
from model import FileSystem
from table import SystemFileTable
from block import FAT


ACCESS_MODE = {
	'c' : 0x8,
	'd' : 0x4,
	'w' : 0x2,
	'r' : 0x1
}


UPDATE_MODE = {
	'a' : 0x2,
	'e' : 0x1
}


BASE_PATH = '.root'
USER_PATH = '.config/user.xml'


class Singleton(object):
	"""
	the module config class, and is singleton design pattern
	include shared variable between the whole project
	"""
	__instance = None

	def __init__(self):
		self.current_user = None
		self._manager = UserManager()
		self._table = SystemFileTable()
		self._fat = FAT(1024)

	@property
	def user(self):
		return self.current_user

	@property
	def manager(self):
		""" return user manager """
		return self._manager

	def set_user(self, user):
		self.current_user = user

	@property
	def table(self):
		return self._table

	@property
	def fat(self):
		return self._fat

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance


class System(object):
	"""
	the class define the singleton file system shared by all module
	"""
	__instance = None

	def __init__(self):
		self.file_system = FileSystem()

	@property
	def system(self):
		return self.file_system

	@property
	def path(self):
		return self.file_system.path

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = System()
		return cls.__instance
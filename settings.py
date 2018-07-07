"""
config the project setting
and construct the global variable
"""
from user_manage import UserManager


ACCESS_MODE = {
	'c' : 0x8,
	'd' : 0x4,
	'w' : 0x2,
	'r' : 0x1
}


class Singleton(object):
	"""
	the module config class, and is singleton design pattern
	include shared variable between the whole project
	"""
	__instance = None

	def __init__(self):
		self.current_user = None
		self._manager = UserManager()

	@property
	def user(self):
		return self.current_user

	@property
	def manager(self):
		return self._manager

	def set_user(self, user):
		print(user)
		self.current_user = user

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance
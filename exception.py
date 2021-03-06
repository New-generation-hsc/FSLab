"""
This module define the Exception that may be raise 
by user operation
"""
import surface

class CmdNotFound(Exception):
	"""
	Command not found
	"""
	def __init__(self, message, cmd):
		super(CmdNotFound, self).__init__(message)
		self.cmd = cmd

	def print_error(self):
		msg = "{}: command not exists".format(self.cmd)
		surface.print_error(msg)


class PathException(Exception):
	"""
	when change path, but the given path is not valid
	"""
	def __init__(self, message, path):
		super(PathException, self).__init__(message)
		self.path = path

	def print_error(self):
		msg = "{}: not a valid path".format(self.path)
		surface.print_error(msg)


class ArgumentException(Exception):
	"""
	the command argument not valid
	"""
	def __init__(self, message, args):
		super(ArgumentException, self).__init__(message)
		self.args = args

	def print_error(self):
		msg = "{}: not a valid argumentent".format(self.args)
		surface.print_error(msg)


class PermissionDeny(Exception):
	"""
	access permission is not enough
	"""
	def __init__(self, message, permission):
		super(PermissionDeny, self).__init__(message)
		self.permission = permission

	def print_error(self):
		add = (self.permission & 0x20) >> 5
		erase = (self.permission & 0x10) >> 4
		create = (self.permission & 0x8) >> 3
		delete = (self.permission & 0x4) >> 2
		write = (self.permission & 0x2) >> 1
		read = self.permission & 0x1
		msg = "!Permission Deny; `{}` permission are need".format('add' * add + 'erase' * erase + 'create' * create + 'delete' * delete + 'write' * write + 'read' * read)
		surface.print_error(msg)


class AuthenticationException(Exception):
	"""
	login required
	"""
	def print_error(self):
		msg = "Authenticate failed. Check username or password"
		surface.print_error(msg)


class ArgumentError(Exception):
	"""
	argparse parse failed
	"""
	def __init__(self, message, cmd):
		super(ArgumentError, self).__init__(message)
		self.cmd = cmd

	def print_error(self):
		surface.print_error("Argument Not Valid")
		self.cmd.print_help()


class ArgumentParserError(Exception):
	pass


class FileAccessException(Exception):
	"""
	you can only write and read an already opened file.
	"""
	def __init__(self, message, path):
		super(FileAccessException, self).__init__(message)
		self.path = path

	def print_error(self):
		surface.print_error("!File Access Deny, please check `{}` is opened".format(self.path))
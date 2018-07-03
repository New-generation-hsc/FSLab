"""
This module define the Exception that may be raise 
by user operation
"""

class CmdNotFound(Exception):
	"""
	Command not found
	"""
	pass

class PathException(Exception):
	"""
	when change path, but the given path is not valid
	"""
	pass


class ArgumentException(Exception):
	"""
	the command argument not valid
	"""
	pass
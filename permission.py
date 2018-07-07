"""
The module define the user permission management
include : 
`grant` permission
`revoke` permission
`check` permission
"""
from settings import ACCESS_MODE, Singleton
from exception import PermissionDeny, AuthenticationException
from functools import wraps


# permission request 
def request(mode, file):
    access = list(mode)
    permission = 0x0;
    for char in access:
        bin_permission = ACCESS_MODE.get(char, 0x0)
        permission |= bin_permission
    assert Singleton.getInstance().user != None
    if (file.permission[Singleton.getInstance().user.name] & permission) != permission:
        raise PermissionDeny("Permission Not Enough")


# login require decorator
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not Singleton.getInstance().user:
            raise AuthenticationException("login required")
        print(args, kwargs)
        f(*args, **kwargs)
    return wrapper


class Permission(object):
    """permission management
    access mode : `c`, `d`, `w`, `r`
    `c` : create file and directory
    `d` : delete file and directory
    `w` : write to file
    `r` : read content from file
    access mode is `cdwr` representation, and is binary representation
    """
    def __init__(self, manager, file_system):
        self.manager = manager

    def grant(self, username, file_name, access_mode):
        """
        grant the specific access_mode to user 
        """
        user = self.manager.search(username)
        file = self.fs.search(file_name)
        if not user or not file:
            return False
        if not (file.belongs == CURRENT_USER):  # current user must have grant permission
            return False
        if file.belongs == user:  # no need grant permission to self
            return True
        file.permission[user.name] = access_mode

"""
The module define the user permission management
include : 
`grant` permission
`revoke` permission
`check` permission
"""
import settings
from exception import PermissionDeny, AuthenticationException
from functools import wraps


# permission request 
def request(mode, file):
    access = list(mode)
    permission = 0x0
    for char in access:
        bin_permission = settings.ACCESS_MODE.get(char, 0x0)
        permission |= bin_permission
    assert settings.Singleton.getInstance().user != None
    if (file.permission(settings.Singleton.getInstance().user.name) & permission) != permission:
        raise PermissionDeny("Permission Not Enough", permission)


# login require decorator
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not settings.Singleton.getInstance().user:
            raise AuthenticationException("login required")
        return f(*args, **kwargs)
    return wrapper


def update_user_permission(mode):
    """ check current user has add or delete user permission whether or not"""
    permission = 0x0
    for char in list(mode):
        bin_permission = settings.UPDATE_MODE.get(char, 0x0)
        permission |= bin_permission
    if (settings.Singleton.getInstance().user.permission & permission) != permission:
        raise PermissionDeny("Permission Not Enough", permission << 4)


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

"""
用户管理员相关模块实现
"""
import settings
from permission import update_user_permission

class User:
    """
    用户类
    """
    def __init__(self, username, password):
        self.name = username
        self._psd = password
        self._permisson = 0x0

    def check_psd(self, password):
        if password == self._psd:
            return True
        return False

    def __repr__(self):
        return "<{}, {}>".format(self.name, self._psd)

    @property
    def permission(self):
        return self._permisson

    def set_permission(self, permission):
        self._permisson = permission

    def to_dict(self):
        return {
            "username" : self.name,
            "password" : self._psd,
            "permission" : self._permisson
        }

    @classmethod
    def get_instance(cls, object_dict):
        instance = cls(object_dict["username"], object_dict["password"])
        instance.set_permission(object_dict["permission"])
        return instance


class UserManager:
    """
    用户管理类
    """
    def __init__(self):
        self.users = []
        user = User("admin", "admin")
        user.set_permission(0x3)
        self.users.append(user)
        self.users.append(User("guest", ""))

    def search(self, username):
        """
        from users search the specific username
        :param username:
        :return: search successfully, return user, else return None
        """

        for user in self.users:
            if user.name == username:
                return user
        return None

    def get_users(self):
        """
        return users not admin and guest
        """
        return list(filter(lambda x : x.name != "admin" and x.name != "guest", self.users))

    def get_user(self, username):
        """
        get the specific user with username
        """
        for user in self.users:
            if user.name == username:
                return user
        return None

    def display(self):
        for user in self.users:
            print(user.name)

    def add_user(self, username, password):
        update_user_permission('a')
        if not self.search(username):
            user = User(username, password)
            self.users.append(user)
            return user
        return None

    def delete_user(self, username):
        update_user_permission('e')
        user = self.search(username)
        if user:
            if user.name != "admin" and user.name == "guest":
                self.users.remove(user)
            return user
        return None

    def login(self, username, password):
        user = self.search(username)
        if user:
            status = user.check_psd(password)
            if status:
                settings.Singleton.getInstance().set_user(user)
            return status
        return False

    def clear(self):
        """
        format: only save 'admin'
        """
        self.users = self.users[:1]
"""
用户管理员相关模块实现
"""
import settings

class User:
    """
    用户类
    """
    def __init__(self, username, password):
        self.name = username
        self._psd = password

    def check_psd(self, password):
        if password == self._psd:
            return True
        return False

    def __repr__(self):
        return "<{}, {}>".format(self.name, self._psd)


class UserManager:
    """
    用户管理类
    """
    def __init__(self):
        self.users = []
        self.users.append(User("admin", "admin"))
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

    def display(self):
        for user in self.users:
            print(user.name)

    def add_user(self, username, password):
        if not self.search(username):
            self.users.append(User(username, password))
            return True
        return False

    def delete_user(self, username):
        user = self.search(username)
        if user:
            if user.name != "admin" and user.name == "guest":
                self.users.remove(user)
            return True
        return False

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
"""
load user to the file system
"""
from convert import xml_to_user, dict_to_xml
import settings
import os

def load_user():
    """
    load user from the disk
    """
    users_dict = xml_to_user(settings.USER_PATH)
    manager = settings.Singleton.getInstance().manager
    table = settings.Singleton.getInstance().table
    for user_dict in users_dict:
        user = manager.add_user(user_dict['username'], user_dict['password'])
        user.set_permission(user_dict['permission'])
        table.add_user(user.name)


def store_user():
    """
    store user in the disk
    """
    users = settings.Singleton.getInstance().manager.get_users()
    users_dict = [user.to_dict() for user in users]
    dict_to_xml(users_dict, settings.USER_PATH, "usermanager", "user")


def recursion_user(root_path, user_name):
    manager = settings.Singleton.getInstance().manager
    fs = settings.System.getInstance().system
    files = os.listdir(root_path)
    for file in files:
        path = os.path.join(root_path, file)
        if os.path.isdir(path):
            node = fs.create_directory(file)
            node.set_belongs(manager.get_user(user_name))
            fs.switch(file)
            recursion_user(path, user_name)
            fs.switch('..')
        else:
            node = fs.create_file(file)
            node.set_belongs(manager.get_user(user_name))


def trans_to_tree(root_path):
    manager = settings.Singleton.getInstance().manager
    user_list = [user.name for user in manager.get_users()]
    fs = settings.System.getInstance().system
    files = os.listdir(root_path)
    for file in files:
        path = os.path.join(root_path, file)
        if file in user_list and os.path.isdir(path):
            fs.create_user_directory(manager.get_user(file))
            fs.switch(file)
            recursion_user(path, file)
            fs.switch('..')
        else:
            if os.path.isfile(path):
                node = fs.create_file(file)
                node.set_belongs(manager.get_user("admin"))
            else:
                node = fs.create_directory(file)
                node.set_belongs(manager.get_user("admin"))
                fs.switch(file)
                recursion_user(path, "admin")
                fs.switch('..')
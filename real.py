"""
This module define the operation with disk using `os` module
and user operation will actually create in disk
"""

import settings
import os
import shutil


def create_file(relative_path):
    """
    create file in the disk
    """
    path = settings.BASE_PATH + relative_path
    file = open(path, mode='w', encoding='utf-8')
    file.close()


def create_directory(relative_path):
    """
    create a directory in the disk
    """
    path = settings.BASE_PATH + relative_path
    os.makedirs(path)


def delete_file(relative_path):
    """
    delete file from disk
    """
    path = settings.BASE_PATH + relative_path
    os.remove(path)


def delete_directory(relative_path):
    """
    delete directory from disk
    """
    path = settings.BASE_PATH + relative_path
    shutil.rmtree(path)


def format_user_directory(user):
    """
    format a user directory
    """
    path = settings.BASE_PATH + '/' + user.name
    shutil.rmtree(path)
    os.makedirs(path)

from model import FileSystem
from user_manage import UserManager

fs = FileSystem()
manager = UserManager()

status = manager.login("admin", "admin")


fs.create_file('file1')
# fs.create_file('file2')
# fs.create_file('file3')
# fs.create_directory('dir1')
# fs.create_directory('dir2')
# fs.switch('dir1')
# fs.create_file('file1')
# fs.create_file('file2')
# fs.create_directory('dir3')
# fs.switch('/')
fs.display()
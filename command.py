"""
This module will contain all command that will be used in cmd
"""
import argparse
from decorator import CmdManager
from decorator import CmdRouter

app = CmdManager()

class ListCmd(CmdRouter):
    """
    `ls` command class:
    include the following usage
    1. `ls` :> list the current path file and directory
    2. `ls` file... :> list the files
    3. `ls` -s :> list files in current path and display them in order
    4. `ls` -f :> just list files in current path exclude directory
    5. `ls` -d :> just list directory in current path exclude files
    6. `ls` -l :> list files detail information
    """
    optional_args = ['-s', '-f', '-d', '-l']

    def __init__(self):
        super(ListCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='ls', usage='%(prog)s [options]')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('-s', action='store_true', help='display files in order')
        self.parser.add_argument('-f', action='store_true', help='display just files')
        self.parser.add_argument('-d', action='store_true', help='display just directory')
        self.parser.add_argument('-l', action='store_true', help='display files information')
        self.parser.add_argument('files', nargs='*', help='the files need to display')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class CdCmd(CmdRouter):
    """
    The Command `cd`, change directory
    the usage example is:
    :> `cd` path
    """
    optional_args = []

    def __init__(self):
        super(CdCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='cd', usage='%(prog)s path')
        self.registe_parser()

    def registe_parser(self):
        self.parser.add_argument('path', help='the location path')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class MkDirCmd(CmdRouter):
    """
    The `mkdir` command : create an new empty directory
    the command usage:
    :> `mkdir` dir1, dir2, dir3...
    """
    optional_args = []

    def __init__(self):
        super(MkDirCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='mkdir', usage='%(prog)s path')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('directory', nargs='+', help='the location path')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class RmCmd(CmdRouter):
    """
    the `rm` command: delete file or directory from current path
    Command Usage:
    :> `rm` file1, file2... : remove file 
    :> `rm` -r dir1 : remove directory
    """
    optional_args = ['-r']

    def __init__(self):
        super(RmCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='rm', usage='%(prog)s [-r] options')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('-r', action='store_true', help='recrusive remove file')
        self.parser.add_argument('path', nargs='+', help='the file and directory that want to delete')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class TouchCmd(CmdRouter):
    """
    the `touch` command: create  new empty file
    Command Usage:
    :> `touch` file1, file2...
    """
    optional_args = []

    def __init__(self):
        super(TouchCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='touch', usage='%(prog)s files')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('files', nargs='+', help='filenaemes that created')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class SuCmd(CmdRouter):
    """
    the 'su' command: switch to the special user
    Command usage:
    :> 'su' username
    """
    optional_args = []

    def __init__(self):
        super(SuCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='su', usage='%(prog)s username')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='switch to special user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class AdduserCmd(CmdRouter):
    """
    the 'adduser' command: add a new user
    Command usage:
    :> 'adduser'
    """
    optional_args = []

    def __init__(self):
        super(AdduserCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='adduser', usage='%(prog)s')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='add a new user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class DeleteuserCmd(CmdRouter):
    """
    the 'deleteuser' command: delete an old user
    Command usage:
    :> 'deleteuser'
    """
    optional_args = []

    def __init__(self):
        super(DeleteuserCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='deleteuser', usage='%(prog)s')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='delete a user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

class CheckuserCmd(CmdRouter):
    """
    the 'checkuser' command: check the current users
    Command usage:
    :> 'checkuser'
    """
    optional_args = []

    def __init__(self):
        super(CheckuserCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='checkuser', usage='%(prog)s')

    def registe_parser(self):
        pass

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class FormatCmd(CmdRouter):
    """
    the 'format' command: format the current_user relative content
    """
    optional_args = []

    def __init__(self):
        super(FormatCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='format', usage='%(prog)s')

    def register_parser(self):
        pass

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


class ClearCmd(CmdRouter):
    """
    the `clear` command:
    clear current screen
    """
    optional_args = []

    def __init__(self):
        super(ClearCmd, self).__init__()
        self.parser = argparse.ArgumentParser(prog='clear', usage='%(prog)s')

    def register_parser(self):
        pass

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())


app.register('ls', ListCmd)
app.register('cd', CdCmd)
app.register('rm', RmCmd)
app.register('mkdir', MkDirCmd)
app.register('touch', TouchCmd)
app.register('su', SuCmd)
app.register('adduser', AdduserCmd)
app.register('deleteuser', DeleteuserCmd)
app.register('checkuser', CheckuserCmd)
app.register('format', FormatCmd)
app.register('clear', ClearCmd)

if __name__ == "__main__":

    app.run('ls')
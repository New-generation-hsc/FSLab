"""
This module will contain all command that will be used in cmd
"""
import argparse
from decorator import CmdManager
from decorator import CmdRouter
from exception import ArgumentParserError
import re

app = CmdManager()


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


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
        self.parser = ThrowingArgumentParser(prog='ls', usage='%(prog)s [options]')
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
        self.parser = ThrowingArgumentParser(prog='cd', usage='%(prog)s path')
        self.registe_parser()

    def registe_parser(self):
        self.parser.add_argument('path', help='the location path')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class MkDirCmd(CmdRouter):
    """
    The `mkdir` command : create an new empty directory
    the command usage:
    :> `mkdir` dir1, dir2, dir3...
    """
    optional_args = []

    def __init__(self):
        super(MkDirCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='mkdir', usage='%(prog)s path')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('directory', nargs='+', help='the location path')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


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
        self.parser = ThrowingArgumentParser(prog='rm', usage='%(prog)s [-r] options')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('-r', action='store_true', help='recrusive remove file')
        self.parser.add_argument('path', nargs='+', help='the file and directory that want to delete')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class TouchCmd(CmdRouter):
    """
    the `touch` command: create  new empty file
    Command Usage:
    :> `touch` file1, file2...
    """
    optional_args = []

    def __init__(self):
        super(TouchCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='touch', usage='%(prog)s files')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('files', nargs='+', help='filenaemes that created')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class SuCmd(CmdRouter):
    """
    the 'su' command: switch to the special user
    Command usage:
    :> 'su' username
    """
    optional_args = []

    def __init__(self):
        super(SuCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='su', usage='%(prog)s username')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='switch to special user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class AdduserCmd(CmdRouter):
    """
    the 'adduser' command: add a new user
    Command usage:
    :> 'adduser'
    """
    optional_args = []

    def __init__(self):
        super(AdduserCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='adduser', usage='%(prog)s')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='add a new user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class DeleteuserCmd(CmdRouter):
    """
    the 'deleteuser' command: delete an old user
    Command usage:
    :> 'deleteuser'
    """
    optional_args = []

    def __init__(self):
        super(DeleteuserCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='deleteuser', usage='%(prog)s')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('username', help='delete a user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()

class CheckuserCmd(CmdRouter):
    """
    the 'checkuser' command: check the current users
    Command usage:
    :> 'checkuser'
    """
    optional_args = []

    def __init__(self):
        super(CheckuserCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='checkuser', usage='%(prog)s')

    def registe_parser(self):
        pass

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class FormatCmd(CmdRouter):
    """
    the 'format' command: format the current_user relative content
    """
    optional_args = ['-u']

    def __init__(self):
        super(FormatCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='format', usage='%(prog)s')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument("-u", nargs='?', help='indicate format a specific user')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class ClearCmd(CmdRouter):
    """
    the `clear` command:
    clear current screen
    """
    optional_args = []

    def __init__(self):
        super(ClearCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='clear', usage='%(prog)s')

    def register_parser(self):
        pass

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class WriteCmd(CmdRouter):
    """
    write file
    """
    optional_args = []

    def __init__(self):
        super(WriteCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='write', usage='%(prog)s file content')
        self.register_parser()
        self.pattern = re.compile(r"(?P<file>\w+) (?P<content>(\".*\"|\w+))")

    def register_parser(self):
        self.parser.add_argument('file', help='write file')
        self.parser.add_argument('content', help='file content')

    def parse_args(self, argument):
        match = self.pattern.search(argument)
        file_name, content = match.group("file"), match.group("content").strip("\"")
        return self.parser.parse_args([file_name, content])

    def print_help(self):
        self.parser.print_help()


class ReadCmd(CmdRouter):
    """
    read file
    """
    optional_args = []

    def __init__(self):
        super(ReadCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='read', usage='%(prog)s file')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('file', help='read file')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class OpenCmd(CmdRouter):
    """
    read file
    """
    optional_args = []

    def __init__(self):
        super(OpenCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='open', usage='%(prog)s file')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('file', help='open file')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class CloseCmd(CmdRouter):
    """
    read file
    """
    optional_args = []

    def __init__(self):
        super(CloseCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='close', usage='%(prog)s file')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('file', help='close file')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class TableCmd(CmdRouter):
    """
    read file
    """
    optional_args = ['-u']

    def __init__(self):
        super(TableCmd, self).__init__()
        self.parser = ThrowingArgumentParser(prog='table', usage='%(prog)s [-u]')
        self.register_parser()

    def register_parser(self):
        self.parser.add_argument('-u', action='store_true',  help='show current user file table')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


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
app.register('write', WriteCmd)
app.register('read', ReadCmd)
app.register('open', OpenCmd)
app.register('close', CloseCmd)
app.register('table', TableCmd)

if __name__ == "__main__":

    app.run('ls')
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
        self.registe_parser()

    def registe_parser(self):
        self.parser.add_argument('-s', action='store_true', help='display files in order')
        self.parser.add_argument('-f', action='store_true', help='display just files')
        self.parser.add_argument('-d', action='store_true', help='display just directory')
        self.parser.add_argument('-l', action='store_true', help='display files information')
        self.parser.add_argument('files', nargs='*', help='the files need to display')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

    def print_help(self):
        self.parser.print_help()


class ErrorCmd(CmdRouter):
    """
    The command Error handle class, include the following error:
    `command not found` : 404
    `command argument error` : 200
    `switch path error` : 500
    """
    optional_args = ['404', '200', '500']

    def parse_args(self, argument):
        return argument

    def build_router(self, path):
        return [path]

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
        self.registe_parser()

    def registe_parser(self):
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
        self.registe_parser()

    def registe_parser(self):
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
        self.registe_parser()

    def registe_parser(self):
        self.parser.add_argument('files', nargs='+', help='filenaemes that created')

    def parse_args(self, argument):
        return self.parser.parse_args(argument.split())

app.registe('ls', ListCmd)
app.registe('error', ErrorCmd)
app.registe('cd', CdCmd)
app.registe('rm', RmCmd)
app.registe('mkdir', MkDirCmd)
app.registe('touch', TouchCmd)

if __name__ == "__main__":

    app.run('ls')
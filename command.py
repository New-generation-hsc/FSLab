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
    """
    optional_args = ['200', '400']

    def parse_args(self, argument):
        return None

    def build_router(self, path):
        return [path]


app.registe('ls', ListCmd)
app.registe('error', ErrorCmd)

if __name__ == "__main__":

    app.run('ls')
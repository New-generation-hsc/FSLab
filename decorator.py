"""
This is moudle where define different decorator
these decorator are responsible for different function
1. Command Router
2. Commnad Register
3. User Permission
"""

import abc
import functools


def hash_argument(argument):

    if(not argument or len(argument) == 0):
        return 0
    hash_str = ''.join(argument)
    hash_code = 0
    for s in hash_str:
        hash_code += ord(s)
    return hash_code


class CmdRouter(object):
    """
    The abstract command decorator, control path route
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.routes = {}

    @abc.abstractmethod
    def parse_args(self, argument):
        raise NotImplementedError("No Need Implementation")

    @abc.abstractmethod
    def registe_parser(self):
        raise NotImplementedError("No Need Implementation")

    def route(self, route_str, f):
        self.routes[hash_argument(route_str)] = f

    def serve(self, path, args):
        func = self.routes.get(hash_argument(path))
        if func :
            func(args)
        else :
            raise NotImplementedError("Not Implemented Yet")

    def build_router(self, path):
        """
        according to the command optional argument and user input command argument
        build the command router
        `cmd_args` :> the build-in command argument
        `namespace` :> the user command argument
        """
        args = []
        namespace = self.parse_args(path)
        for arg in self.optional_args:
            if getattr(namespace, arg[1:]):
                args.append(arg)
        return args


class CmdManager(object):
    """
    Manager all kinds of command, this is the first route layer
    """
    def __init__(self, *args, **kwargs):
        super(CmdManager, self).__init__(*args, **kwargs)
        self.command = {}

    def registe(self, cmd, cls):
        self.command[cmd] = cls()

    def route(self, route_str, cmd):
        def decorator(f):
            instance = self.command.get(cmd)
            if instance:
                instance.route(route_str, f)
            else:
                self.serve('404', 'error')
        return decorator

    def serve(self, path, cmd):
        instance = self.command.get(cmd)
        if instance:
            args = instance.parse_args(path)
            route_path = instance.build_router(path)
            instance.serve(route_path, args)
        else:
            self.serve('200', 'error')

    def run(self, command):
        """
        run the intput command
        """
        space_index = command.find(' ')
        if(space_index == -1):
            space_index = len(command)
        self.serve(command[space_index:], cmd=command[:space_index])
"""Defines abstract versions of tools.

These abcs define a set of apis for the various tools that will be called out
to by the shell commands.
"""

import abc

class TutTool(metaclass=abc.ABCMeta):
    def __init__(self, config):
        """Config is the python dict from the config file, either globally or
        locally.
        """
        self.config = config

    @abc.abstractmethod
    def initialize_environment(self, project_root, dotdir):
        """This should initilize the project environment for the tool.

        As an example, a `git` tool should, in initialize_environment create
        a .git (by initializing a git repo) in project_root, and then
        potentially also create a .gitignore in either the project_root or
        dotdir, depending on some thing.

        This method will be called during (and hopefully only during) the
        invocation of the `init` or `new` subcommands, for every tool.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def register_callback(self, project_root, dotdir, command, cb):
        """Generic way to register a callback on another tool's action.

        For example, the Venv EnvironmentTool might want to register a 
        callback on the generic VCS tool to add something to the ignorefile
        (which is a generic gitignore/hgignore/svn-ignore command).
        """
        raise NotImplementedError()


class EnvironmentTool(TutTool, metaclass=abc.ABCMeta):
    # TODO: make context manager?
    @abc.abstractmethod
    def enter(self, project_root, dotdir):
        """Enter the project environment.

        This would commonly be done by running `source dotdir/bin/activate`,
        but could be handled differently for hypervisor based env management.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def exit(self, project_root, dotdir):
        """Exit the project environment.

        Akin to `deactivate` in venv.
        """
        raise NotImplementedError()


class TestTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def test(self, project_root, dotdir):
        raise NotImplementedError()


class DependencyTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def install(self, project_root, dotdir, dep):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, project_root, dotdir, dep):
        raise NotImplementedError()

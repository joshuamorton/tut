"""Defines abstract versions of tools.

These abcs define a set of apis for the various tools that will be called out
to by the shell commands.
"""

import abc
import os

class TutTool(metaclass=abc.ABCMeta):
    def __init__(self, config, project_root):
        """Config is the python dict from the config file, either globally or
        locally.
        """
        self.config = config
        self.root_dir = project_root

    @abc.abstractmethod
    def initialize_environment(self):
        """This should initilize the project environment for the tool.

        As an example, a `git` tool should, in initialize_environment create
        a .git (by initializing a git repo) in project_root, and then
        potentially also create a .gitignore in either the project_root or
        dotdir, depending on some thing.

        This method will be called during (and hopefully only during) the
        invocation of the `init` or `new` subcommands, for every tool.
        """
        raise NotImplementedError()

    @property
    def tut_dir(self):
        return os.path.join(self.root_dir, '.tut')

    @property
    def tutfile(self):
        return os.path.join(self.tut_dir, '.tutfile')


class EnvironmentTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __enter__(self):
        """Enter the project environment.

        This would commonly be done by running `source dotdir/bin/activate`,
        but could be handled differently for hypervisor based env management.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def __exit__(self, _type, value, traceback):
        """Exit the project environment.

        Akin to `deactivate` in venv.
        """
        raise NotImplementedError()


class TestTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def test(self):
        raise NotImplementedError()


class DependencyTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def install(self, dep):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, dep):
        raise NotImplementedError()


class VCSTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ignore_files(self, *file_regexes):
        raise NotImplementedError()

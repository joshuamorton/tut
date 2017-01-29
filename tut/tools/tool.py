"""Defines abstract versions of tools.

These abcs define a set of apis for the various tools that will be called out
to by the shell commands.
"""

import abc
import os

class TutTool(metaclass=abc.ABCMeta):
    def __init__(self, config, project, project_root):
        """Config is the python dict from the config file, either globally or
        locally.
        """
        self.config = config
        self.root_dir = os.path.abspath(project_root)
        self.project = project

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


class EnvTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, *commands):
        """Run command in the environment.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def run_in_shell(self, *commands):
        """Run a command in the environment, but in shell.

        This should be roughly equivalent to subprocess.call(...,shell=True).
        """
        raise NotImplementedError()

class TestTool(TutTool, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def test(self):
        raise NotImplementedError()


class DepTool(TutTool, metaclass=abc.ABCMeta):
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


class LangTool(TutTool, metaclass=abc.ABCMeta):
    def __init__(self, config, project, project_root):
        super().__init__(config, project, project_root)
        self._version = self.resolve_version(config['version'])
        if 'ignored-tools' in config:
            project.vcs.config['ignored-tools'].extend(config['ignored-tools'])


    @property
    def version(self):
        return self._version

    @abc.abstractmethod
    def resolve_version(self, version_str):
        raise NotImplementedError()

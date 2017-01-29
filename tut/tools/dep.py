import tools.tool
import os
import pexpect

class RequirementsTool(tools.tool.DepTool):
    def install(self, dep):
        self.project.env.run('pip install {}'.format(dep))
        print(self.root_dir)
        self.project.env.run_in_shell('pip freeze > {}'.format(
            os.path.join(self.root_dir, 'requirements.txt')))

    def update(self, dep):
        raise NotImplementedError()

    def initialize_environment(self):
        pass

class PipenvTool(tools.tool.DepTool):
    def __init__(self, config, project, root_dir):
        super().__init__(config, project, root_dir)
        self.project.env.env_dir = os.path.join(
                self.project.env.root_dir, '.venv')

        self.project.vcs.config['ignored-files'].append('.venv')

    def initialize_environment(self):
        old_dir = os.getcwd()
        os.chdir(self.project.root_dir)
        if self.project.config['python']['version'] >= 3:
            pexpect.run('pipenv --three')
        else:
            pexpect.run('pipenv --two')
        pexpect.run('pipenv install')
        os.chdir(old_dir)

    def install(self, dep):
        """Note that this allows generic passthrough to pipenv, meaning that
        things like `tut install --dev pytest` should work as expected.
        """
        pexpect.run('pipenv install {}'.format(dep))

    def update(self, dep):
        pass

import tools.tool
import os

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

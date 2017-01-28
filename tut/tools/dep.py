import tools.tool

class RequirementsTool(tools.tool.DepTool):
    def install(self, dep):
        self.project.env.run('pip install {}'.format(dep))
        self.project.env.run('pip freeze -r {}/requirements.txt'.format(self.root_dir))

    def update(self, dep):
        raise NotImplementedError()

    def initialize_environment(self):
        pass

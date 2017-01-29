import os
import tools.tool

class PytestTool(tools.tool.TestTool):
    def initialize_environment(self):
        os.mkdir(os.path.join(self.root_dir, 'test'))
        self.project.dep.install('pytest')

    def test(self):
        print(self.project.env.run(
            'pytest {}'.format(os.path.join(self.root_dir, 'test'))))

import subprocess
import os
import pexpect

import tools.tool


class VenvTool(tools.tool.EnvTool):
    def __init__(self, config, project, root_dir):
        super().__init__(config, project, root_dir)
        self.child = None
    
    def initialize_environment(self):
        subprocess.check_call(['python3', '-m', 'venv', self.root_dir])

    def run(self, *commands):
        commands = list(commands)
        print(os.getcwd())
        commands[0] = self.root_dir + '/bin/' + commands[0]
        return pexpect.run(' '.join(commands)).decode()

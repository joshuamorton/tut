import subprocess
import pexpect

import tools.tool


class VenvTool(tools.tool.EnvironmentTool):
    def __init__(self, config, root_dir):
        super().__init__(config, root_dir)
        self.child = None
    
    def initialize_environment(self):
        subprocess.check_call(['python3', '-m', 'venv', self.root_dir])

    def __enter__(self):
        self.child = pexpect.spawn('source bin/activate')
        return self.child

    def __exit__(self, _type, value, traceback):
        self.child.close()

import os
import subprocess
import requests

import tools.tool

class GitTool(tools.tool.VCSTool):
    def initialize_environment(self):
        """Sets up a git repository in the directory.
        """
        subprocess.check_call(['git', 'init', '--quiet', self.root_dir])
        gitignore_path = os.path.join(self.root_dir, '.gitignore')
        with open(gitignore_path, 'w') as gitignore:
            text = requests.get('https://gitignore.io/api/{}'.format(
                '.'.join(self.config['gi-types']))).text
            gitignore.write(text)

        with open(gitignore_path, 'a') as gitignore:
            gitignore.write('\n'.join(self.config['ignored-files']))

    def ignore_files(self, *file_regexs):
        self.config['ignored-files'] += file_regexs

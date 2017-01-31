import shutil
import subprocess

from tut.tools import tool

class PythonTool(tool.LangTool):
    def resolve_version(self, version_identifier):
        version = None
        if version_identifier in {'default', 'python'}:
            version = self._get_ver_from_env('python')
        elif version_identifier in {'python3', '3', 3}:
            version = self._get_ver_from_env('python3')
        elif version_identifier in {'python2', '2', 2}:
            version = self._get_ver_from_env('python2')
        else:
            version = str(version_identifier)
        return version

    @staticmethod
    def _get_ver_from_env(version_string):
        return subprocess.check_output(
                [shutil.which(version_string), '--version'])[-5:]

    @staticmethod
    def is_newer(v1, v2):
        v1_split = [int(x) for x in v1.split('.')]
        v2_split = [int(x) for x in v2.split('.')]
        if len(v1_split) < len(v2_split):
            v1_split.extend([0] * (len(v2_split) - len(v1_split)))
        return v1_split < v2_split


    def initialize_environment(self):
        """Ensure python is availible in our environment.
        """
        python_version = self.project.env.run('python --version').strip()[-5:]
        if self.version[0] != python_version[0]:
            raise EnvironmentError('Your environment was instantiated with'
                    'python2 but you requested python3')
        if not self.is_newer(self.version, python_version):
            raise EnvironmentError('Your environment was instantiated with'
                    'an older version of python than you expected')



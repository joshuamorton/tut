import unittest
import os
import toml
from unittest import mock


from click.testing import CliRunner
import tut

class TutCLITest(unittest.TestCase):
    def test_basic_config(self):
        runner = CliRunner()
        with open('test/tutfiles/default.global') as tutfile:
            m = mock.mock_open(read_data=tutfile.read())
            mock_response = mock.MagicMock()
            mock_response.text = 'mock_gitignore_data'
            r = mock.MagicMock(return_value=mock_response)
        with runner.isolated_filesystem() as fs:
            with mock.patch('builtins.open', m), mock.patch('requests.get', r):
                result = runner.invoke(
                        tut.interface.cli, ['new', 'project_name', '--real'])
            assert result
            assert os.listdir(fs) == ['project_name']
            files = {'pyvenv.cfg', 'bin', 'lib', 'lib64', 
                    'include',  # venv files
                    '.git',  # git directory
                    'test',  # test directory
                    'requirements.txt'}  # requirements file
                    # normally there would also be
                    # .tutconfig.local
                    # .gitignore
                    # in addition to the above files

            # because we are mocking the open calls in the calls to the tool,
            # we need to check that .gitignore was created via some other
            # method.
            assert m.mock_calls[4][1][1] == 'w'
            assert m.mock_calls[6][1][0] == 'mock_gitignore_data'
            assert m.mock_calls[8][1][1] == 'a'
            assert m.mock_calls[10][1][0] == ''
            assert m.mock_calls[12][1][0] == 'project_name/.tutconfig.local'
            assert m.mock_calls[12][1][1] == 'w'
            local_config = toml.loads(m.mock_calls[15][1][0])
            assert local_config['python']['version'] > 3
            assert local_config['git']['ignored-files'] == []
            assert local_config['tools'] == {
                    'vcs': 'git', 'env': 'venv', 'lang': 'python',
                    'dep': 'requirements', 'test': 'pytest'
                    }
            fs_files = set(os.listdir(os.path.join(fs, 'project_name')))
            assert files == fs_files


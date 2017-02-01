import os
import toml
import unittest
from unittest import mock


from click.testing import CliRunner
import tut
import test.utils

class TutCLITest(unittest.TestCase):
    def test_basic_config(self):
        runner = CliRunner()
        with open('test/tutfiles/default.global') as tutfile:
            data = tutfile.read()
        mock_response = mock.MagicMock()
        mock_response.text = 'mock_gitignore_data'
        r = mock.MagicMock(return_value=mock_response)
        with runner.isolated_filesystem() as fs:
            p = test.utils.conditionally_mock_open(fs, read_data=data)
            with mock.patch('builtins.open', p), mock.patch('requests.get', r):
                result = runner.invoke(
                        tut.interface.cli, ['new', 'project_name', '--real'])
            assert result
            assert os.listdir(fs) == ['project_name']
            files = {'pyvenv.cfg', 'bin', 'lib', 'lib64', 
                    'include',  # venv files
                    '.git', '.gitignore',  # git directory
                    'test',  # test directory
                    'requirements.txt',
                    '.tutconfig.local'}  # requirements file
                    # normally there would also be
                    # in addition to the above files

            # because we are mocking the open calls in the calls to the tool,
            # we need to check that .gitignore was created via some other
            # method.
            
            fs_files = set(os.listdir(os.path.join(fs, 'project_name')))
            assert files == fs_files
            with open(os.path.join(fs, 'project_name/.tutconfig.local')) as f:
                local_config = toml.load(f)
            assert local_config['python']['version'] > 3
            assert local_config['git']['ignored-files'] == []
            # this is actually an important check, since it is one of the
            # few things that isn't just a straight copy paste.
            assert local_config['git']['ignored-tools'] == ['vim', 'python']
            assert local_config['tools'] == {
                    'vcs': 'git', 'env': 'venv', 'lang': 'python',
                    'dep': 'requirements', 'test': 'pytest'
                    }
            with open(os.path.join(fs, 'project_name/requirements.txt')) as f:
                assert 'pytest' in f.read()


from tut.tools import vcs
from tut.tools import env
from tut.tools import lang
from tut.tools import dep
from tut.tools import test

EVALUATION_ORDER = ['vcs', 'env', 'lang' ,'dep', 'test']

TOOL_MAPPING = {
        'vcs': {
            'git': vcs.GitTool,
            'hg': None
            },
        'env': {
            'venv': env.VenvTool,
            },
        'lang': {
            'python': lang.PythonTool,
            },
        'dep': {
            'requirements': dep.RequirementsTool,
            'pipenv': dep.PipenvTool,
            },
        'test': {
            'pytest': test.PytestTool
            }
        }

import tools.vcs
import tools.env
import tools.lang
import tools.dep
import tools.test

EVALUATION_ORDER = ['vcs', 'env', 'lang' ,'dep', 'test']

TOOL_MAPPING = {
        'vcs': {
            'git': tools.vcs.GitTool,
            'hg': None
            },
        'env': {
            'venv': tools.env.VenvTool,
            },
        'lang': {
            'python': tools.lang.PythonTool,
            },
        'dep': {
            'requirements': tools.dep.RequirementsTool,
            },
        'test': {
            'pytest': None
            }
        }

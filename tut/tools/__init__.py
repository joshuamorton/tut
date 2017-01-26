import tools.vcs
import tools.environment
import tools.lang
import tools.dependency
import tools.test

EVALUATION_ORDER = ['vcs', 'environment', 'lang' ,'dependency', 'test']

TOOL_MAPPING = {
        'vcs': {
            'git': tools.vcs.GitTool,
            'hg': None
            },
        'environment': {
            'venv': tools.environment.VenvTool,
            },
        'lang': {
            'python': None
            },
        'dependency': {
            'requirements': None
            },
        'test': {
            'pytest': None
            }
        }

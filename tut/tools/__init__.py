import tools.vcs
import tools.environment
import tools.language
import tools.dependency
import tools.test

EVALUATION_ORDER = ['vcs', 'environment', 'language' ,'dependency', 'test']

TOOL_MAPPING = {
        'vcs': {
            'git': tools.vcs.GitTool,
            'hg': None
            },
        'environment': {
            'venv': None
            },
        'language': {
            'python': None
            },
        'dependency': {
            'requirements': None
            },
        'test': {
            'pytest': None
            }
        }

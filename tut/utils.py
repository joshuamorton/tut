import os
import toml

def interactive_config_data():
    raise NotImplementedError('not done yet')

def find_global_config():
    if os.path.isfile(os.path.expanduser('~/.config/.tutconfig')):
        # this probably needs to be changed to what is should actually be
        # TODO
        config_location = '~/.config/.tutconfig'
    elif os.path.isfile(os.path.expanduser('~/.tutconfig')):
        config_location = '~/.tutconfig'
    else:
        config_location = None
    return config_location

def parse_config_file(config_location):
    try:
        with open(os.path.expanduser(config_location), 'r') as cfg:
            config_data = toml.loads(cfg.read())
    except FileNotFoundError:
        print("{} is not a valid configuration folder"
                .format(config_location))
    return config_data

def resolve_location(path):
    if os.path.isfile(os.path.expanduser(path)):
        return os.path.expanduser(path)

def find_project_root(dir=None):
    if dir:
        cwd = os.path.abspath(dir)
    else:
        cwd = os.path.abspath(os.getcwd())
    current_dir = cwd
    project_root = None
    while project_root is None:
        if '.tutconfig.local' in os.listdir(current_dir):
            project_root = current_dir
        current_dir = os.path.split(current_dir)[0]
    if not project_root:
        raise Exception('Cannot find project root')
    return project_root

def find_local_config(dir):
    root_dir = find_project_root(dir)
    config_path = os.path.join(root_dir, '.tutconfig.local')
    with open(config_path) as f:
        config = toml.load(f)

    return config

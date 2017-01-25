import os
import toml

def interactive_config_data():
    raise NotImplementedError('not done yet')

def resolve_config(config_dir):
    config_location = None
    if config_dir is not None:
        config_location = config_dir
    elif os.path.isfile(os.path.expanduser('~/.config/.tutconfig')):
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

import click
import os

import utils

@click.group()
def cli():
    """A tool to manage python projects.
    """
    pass

@cli.command()
@click.argument('directory')
@click.option('--config-file', default=None, 
        help='Absolute path to the configuration file.')
def init(directory, config_file=None):
    """Create a new project in an existing folder.
    """
    config_location = utils.resolve_config(config_file)
    print(config_location, directory)

@cli.command()
@click.argument('directory')
@click.option('--config-file', default=None, 
        help='Absolute path to the configuration file.')
def new(directory, config_file=None):
    """Create a new project from scratch.

    Creates a new project in the folder specified by DIRECTORY.
    """

    print('creating new project in {}'.format(os.path.join(os.getcwd(), directory)))
    config_location = utils.resolve_config(config_file)
    if config_location:
        print('using config folder: ' + config_location)
        config_data = utils.parse_config_file(config_location)
    else:
        config_data = utils.interactive_config_data()

    for tool in config_data:
        print(tool)

@cli.command()
def shell():
    """Spawn an interactive shell inside the project environment.
    """
    pass

@cli.command()
def run():
    """Run a single command in the project environment.
    """
    pass

@cli.command()
def install():
    """Install a project dependency in the project environment.
    """
    pass

@cli.command()
def test():
    """Run project tests and report results.
    """
    pass

if __name__ == '__main__':
    cli()

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
    click.echo(directory)

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
        config_data = utils.interactive_plugins()

    for plugin in config_data:
        print(plugin)

if __name__ == '__main__':
    cli()

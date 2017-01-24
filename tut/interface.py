import click
import json
import sys
import os
import toml
import utils

settings = {}


@click.group()
@click.option('--config', default=None, 
        help='Absolute path to the configuration file.')
def cli(config):
    if config is not None:
        settings['config'] = config
    elif os.path.isfile(os.path.expanduser('~/.config/.tutconfig')):
        settings['config'] = '~/.config/.tutconfig'
    elif os.path.isfile(os.path.expanduser('~/.tutconfig')):
        settings['config'] = '~/.tutconfig'
    else:
        settings['config'] = None

@cli.command()
@click.argument('directory')
def init(directory):
    """Create a new project in an existing folder.
    """
    click.echo(directory)

@cli.command()
@click.argument('directory')
def new(directory):
    """Create a new project from scratch.

    Creates a new project in the folder specified by DIRECTORY.
    """
    print('creating new project in {}'.format(os.path.join(os.getcwd(), directory)))
    print(settings)
    if settings['config']:
        print('using config folder: ' + settings['config'])
        try:
            with open(os.path.expanduser(settings['config']), 'r') as cfg:
                settings['plugins'] = toml.loads(cfg.read())
        except FileNotFoundError:
            click.echo("{} is not a valid configuration folder"
                    .format(settings['config']))
    else:
        settings['plugins'] = utils.interactive_plugins()

    for plugin in settings['plugins']:
        print(plugin)

if __name__ == '__main__':
    cli()

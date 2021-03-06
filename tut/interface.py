import os

import click

import toml
import tut.project as project
import tut.utils as utils


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
@click.option('--vcs', '-v',
        type=click.Choice(['git', 'hg']),
        help='Specify nondefault version control software.')
@click.option('--lang', '-l',
        type=click.Choice(['python']),
        help='Specify nondefault python version.')
@click.option('--env', '-e',
        type=click.Choice(['venv', 'virtualenv', 'conda', 'docker']),
        help='Specify nondefault virtual environment tool.')
@click.option('--dep', '-d',
        type=click.Choice(['requirements', 'pipenv']),
        help='Specify nondefault dependency management tool.')
@click.option('--test', '-t',
        type=click.Choice(['pytest', 'unittest', 'nose', 'tox']),
        help='Specify nondefault testing framework.')
@click.option('--unreal', 'modify', flag_value=False, default=True)
@click.option('--real', 'modify', flag_value=True)
def new(directory, modify, config_file=None, **build_tools):
    """Create a new project from scratch.

    Creates a new project in the folder specified by DIRECTORY.
    This project will be configured according to your global tut file, unless
    you specify a nondefault config or a different tool.
    """

    default_config = utils.find_global_config()
    settings = dict()
    if default_config:
        settings = utils.parse_config_file(default_config)

    if config_file:
        local_config = utils.resolve_location(config_file)
        settings.update(utils.parse_config_file(local_config))

    settings['tools'].update({k: v for k, v in build_tools.items() if v})

    proj = project.Project(settings, directory)


    if modify:
        # actually modify the filesystem, but only if the flag is active
        proj.initialize_environment()

        print('writing out local config')
        tutconfig_path = os.path.join(proj.root_dir, '.tutconfig.local')
        with open(tutconfig_path, 'w') as l:
            toml.dump(settings, l)

@cli.command()
def shell():
    """Spawn an interactive shell inside the project environment.
    """
    pass

@cli.command()
@click.argument('commands', nargs=-1)
def run(commands):
    """Run a single command in the project environment.
    """
    local_config = utils.find_local_config(os.getcwd())
    proj = project.Project(local_config)
    proj.env.run(*commands)


@cli.command()
@click.argument('deps', nargs=-1)
def install(deps):
    """Install a project dependency in the project environment.
    """
    local_config = utils.find_local_config(os.getcwd())
    proj = project.Project(local_config)
    for dep in deps:
        proj.dep.install(dep)


@cli.command()
def test():
    """Run project tests and report results.
    """
    local_config = utils.find_local_config(os.getcwd())
    proj = project.Project(local_config)
    proj.test.test()

if __name__ == '__main__':
    cli()

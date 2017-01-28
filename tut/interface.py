import click
import os

import utils
import tools
import project

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
        type=click.Choice([]),
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

    project_tools = dict()
    proj = project.Project()

    for tool in tools.EVALUATION_ORDER:
        # this is the actual loop that will run everything
        choice = settings['tools'][tool]
        print("Using {} as {} tool.".format(choice, tool))
        if tools.TOOL_MAPPING[tool][choice] is not None:
            if choice not in settings:
                settings[choice] = {}
            project_tools[tool] = tools.TOOL_MAPPING[tool][choice](
                    settings[choice], proj, directory)
            proj.register_tool(tool, project_tools[tool])
            print('\t' + str(project_tools[tool]))

    print()
    for plugin in settings['plugins']:
        print(plugin, settings['plugins'][plugin])

    if modify:
        print('modifying file structure')
        os.mkdir(os.path.join(os.getcwd(), directory))
        for tool in tools.EVALUATION_ORDER:
            if tool in project_tools:
                project_tools[tool].initialize_environment()

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

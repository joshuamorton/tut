import tools
import utils
import os

class Project():

    def __init__(self, config, root_dir=None):
        self.root_dir = root_dir or utils.find_project_root()
        self._evaluation_order = tools.EVALUATION_ORDER
        self._mapping = tools.TOOL_MAPPING
        self.config = config
        self.tools = {}
        self.vcs = None
        self.env = None
        self.lang = None
        self.dep = None
        self.test = None

        for tool in self._evaluation_order:
            choice = self.config['tools'][tool]
            print("Using {} as {} tool.".format(choice, tool))
            if self._mapping[tool][choice] is not None:
                if choice not in self.config:
                    self.config[choice] = {}
                self.tools[tool] = self._mapping[tool][choice](
                        self.config[choice], self, self.root_dir)
                self._register_tool(tool, self.tools[tool])
                print('\t' + str(self.tools[tool]))

        print()
        

        for plugin in self.config['plugins']:
            print(plugin, self.config['plugins'][plugin])


    def _register_tool(self, role, obj):
        self.__setattr__(role, obj)

    def initialize_environment(self):
        os.mkdir(self.root_dir)
        for tool in self._evaluation_order:
            if tool in self.tools:
                self.tools[tool].initialize_environment()


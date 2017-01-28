class Project():
    def __init__(self):
        self.vcs = None
        self.env = None
        self.lang = None
        self.dep = None
        self.test = None

    def register_tool(self, role, obj):
        self.__setattr__(role, obj)

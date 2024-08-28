class InvalidCommandBase:
    NAME: str = None

    def __init__(self, tag, value):
        self.__tag = tag
        self.__value = value

    def validate(self) -> bool:
        raise NotImplementedError("Necessary method for Command class")

    @property
    def name(self) -> str:
        return self.NAME

    @property
    def tag(self) -> str:
        return self.__tag

    @property
    def value(self) -> str:
        return self.__value

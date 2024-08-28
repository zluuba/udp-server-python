class CommandBase:
    TAG: str = None
    NAME: str = None

    def __init__(self, value):
        self.__value = value

    def validate(self) -> bool:
        raise NotImplementedError("Necessary method for Command class")

    @property
    def name(self) -> str:
        return self.NAME

    @property
    def tag(self) -> str:
        return self.TAG

    @property
    def value(self) -> str:
        return self.__value

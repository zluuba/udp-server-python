from .base import CommandBase


class UnknownCMD(CommandBase):
    __NAME: str = 'unknown'

    def __init__(self, tag, value):
        super().__init__(
            tag=tag,
            name=self.__NAME,
            value=value,
        )

    def _validate(self):
        return False

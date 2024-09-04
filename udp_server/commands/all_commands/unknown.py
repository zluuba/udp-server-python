from .base import CommandBase


class UnknownCMD(CommandBase):
    __NAME: str = 'unknown'

    def __init__(self, tag, value):
        super().__init__(
            tag=tag,
            name=self.__NAME,
            value=value,
        )

    @property
    def is_valid(self):
        if self._is_valid is None:
            self._is_valid = self._validate()

        return self._is_valid

    def _validate(self):
        return False

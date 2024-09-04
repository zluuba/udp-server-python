from .base import CommandBase


class NetworkTagCMD(CommandBase):
    __TAG: int = 0x1
    __NAME: str = 'network tag'
    __MAX_BYTES: int = 255

    def __init__(self, value):
        super().__init__(
            tag=self.__TAG,
            name=self.__NAME,
            value=value,
        )

    @property
    def is_valid(self):
        if self._is_valid is None:
            self._is_valid = self._validate()

        return self._is_valid

    def _validate(self):
        return len(self.value) <= self.__MAX_BYTES

from .base import CommandBase


class AmplifierSupplyCMD(CommandBase):
    __TAG: int = 0x0
    __NAME: str = 'amplifier supply'
    __ALLOWED_VALUES: list[bytes] = [b'0', b'1']

    def __init__(self, value):
        super().__init__(
            tag=self.__TAG,
            name=self.__NAME,
            value=value,
        )

    def _validate(self):
        return self.value in self.__ALLOWED_VALUES

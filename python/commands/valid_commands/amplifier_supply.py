from commands.valid_commands.base import CommandBase


class AmplifierSupplyCmd(CommandBase):
    TAG: str = '0x0'
    NAME: str = 'питание усилителя'
    _allowed_values: list = ['0', '1']

    def validate(self):
        return self.value in self._allowed_values

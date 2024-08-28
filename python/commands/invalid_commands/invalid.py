from commands.invalid_commands.base import InvalidCommandBase


class InvalidCmd(InvalidCommandBase):
    NAME: str = 'Invalid'

    def validate(self):
        return False

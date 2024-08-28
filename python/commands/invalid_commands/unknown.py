from commands.invalid_commands.base import InvalidCommandBase


class UnknownCmd(InvalidCommandBase):
    NAME: str = 'Unknown'

    def validate(self):
        return False

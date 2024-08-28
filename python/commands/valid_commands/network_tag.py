from commands.valid_commands.base import CommandBase


class NetworkTagCmd(CommandBase):
    TAG: str = '0x1'
    NAME: str = 'метка сети'

    def validate(self):
        return self.is_within_255_bytes(self.value)

    @staticmethod
    def is_within_255_bytes(string: str) -> bool:
        byte_length = len(string.encode('utf-8'))
        return byte_length <= 255

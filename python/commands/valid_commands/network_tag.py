from commands.valid_commands.base import CommandBase


class NetworkTagCmd(CommandBase):
    TAG: str = '0x1'
    NAME: str = 'метка сети'
    MAX_BYTES: int = 255

    def validate(self):
        return self.is_within_max_bytes()

    def is_within_max_bytes(self) -> bool:
        byte_length = len(self.string.encode('utf-8'))
        return byte_length <= self.MAX_BYTES

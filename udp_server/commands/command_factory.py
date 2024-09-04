from .command_map import COMMANDS_MAP
from .all_commands.unknown import UnknownCMD


def command_factory(packet):
    if packet.tag not in COMMANDS_MAP:
        return UnknownCMD(packet.tag, packet.value)

    command_func = COMMANDS_MAP[packet.tag]
    command = command_func(packet.value)
    return command

from .commands_map import COMMANDS_MAP
from .invalid_commands.invalid import InvalidCmd
from .invalid_commands.unknown import UnknownCmd


def command_factory(packet):
    if packet.tag not in COMMANDS_MAP:
        return UnknownCmd(packet.tag, packet.value)

    command_func = COMMANDS_MAP[packet.tag]
    command = command_func(packet.value)

    if not command.validate():
        return InvalidCmd(packet.tag, packet.value)

    return command

from commands.valid_commands.amplifier_supply import AmplifierSupplyCmd
from commands.valid_commands.network_tag import NetworkTagCmd


COMMANDS_MAP = {
    '0x0': AmplifierSupplyCmd,
    '0x1': NetworkTagCmd,
}

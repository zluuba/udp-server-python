from .all_commands.amplifier_supply import AmplifierSupplyCMD
from .all_commands.network_tag import NetworkTagCMD


COMMANDS_MAP = {
    0: AmplifierSupplyCMD,
    1: NetworkTagCMD,
}

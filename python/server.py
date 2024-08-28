from sys import stderr

from commands.command_factory import command_factory
from config import Config
from protocols.udp import UdpPacket
from utils.socket import create_socket
from utils.common import are_commands_valid


def main():
    config = Config()
    sock = create_socket(config)

    while True:
        data, addr = sock.recvfrom(config.mtu)
        udp_packet = UdpPacket(data)

        commands = []
        for data_chunk in udp_packet.data:
            command = command_factory(data_chunk)
            commands.append(command)

            if not command.validate():
                continue

            stderr.write(f'Operation "{command.name}" was successfully completed.\n')

        if (not udp_packet.errors) and are_commands_valid(commands):
            sock.sendto(data, addr)
            continue

        if udp_packet.errors:
            stderr.write(f'UDP Packet has errors: {udp_packet.errors}.\n')
        else:
            stderr.write(f'Some commands was invalid.\n')


if __name__ == '__main__':
    main()

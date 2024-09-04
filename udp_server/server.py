from sys import stderr

from commands.command_factory import command_factory
from commands.command_pool import CommandPool
from config import Config
from errors.error_handler import handle_errors
from protocols.udp import UdpPacket
from utils.socket import (
    create_socket,
    get_data_and_addr_from_socket,
    send_client_data_back,
)


@handle_errors
def run_server(config, sock):
    while True:
        bytes_data, address = get_data_and_addr_from_socket(sock, config.mtu)
        udp_packet = UdpPacket(bytes_data)

        # TODO: move that to function and keep only:
        #       command_pool = get_command_pool() or
        #       command_pool = parse_udp_data() or smth
        command_pool = CommandPool()
        for data_chunk in udp_packet.data:
            command = command_factory(data_chunk)
            command_pool.add(command)
            command.run()

        if udp_packet.errors:
            stderr.write(f'UDP Packet has errors: {udp_packet.errors}.\n')
        elif invalid_commands := command_pool.get_invalid():
            stderr.write(f'Some commands was invalid:\n')
            [stderr.write(f'   {cmd.name}, {cmd.tag}, {cmd.value}\n')
                for cmd in invalid_commands]
        else:
            send_client_data_back(sock, bytes_data, address)


if __name__ == '__main__':
    config = Config()
    sock = create_socket(config)
    run_server(config, sock)

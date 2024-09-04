from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from typing import Any

from config import Config
from errors.exceptions.socket_exceptions import (
    AddressAlreadyInUse,
    ReceiveFromFailure,
    SendToFailure,
)
from utils.traceback import get_error_frame_summary


def create_socket(config: Config) -> socket:
    """
    Create and bind a UDP socket based on the provided configuration.
    Used AF_INET for IPv4 addresses and SOCK_DGRAM for UDP connection.
    Set the SO_REUSEADDR flag that tells the kernel to reuse a local socket
    immediately.

    :param config: configuration of the current server state
    :return: socket object

    :raise: AddressAlreadyInUse exception if socket binding fail
    """

    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((config.ip_address, config.port))
        return sock
    except OSError:
        error_frame_summary = get_error_frame_summary()
        raise AddressAlreadyInUse(
            config.ip_address,
            config.port,
            error_frame_summary,
        )


def close_socket(sock: socket):
    """
    Close a socket file descriptor.

    :param sock: socket object
    """

    sock.close()
    # print('sock was closed')


def get_data_and_addr_from_socket(sock: socket,
                                  data_chunk_size: int
                                  ) -> tuple[bytes, Any]:
    """
    Receive data from the socket.

    :param sock: socket object
    :param data_chunk_size: MTU size
    :return: tuple (bytes, address), where bytes is a bytes object
        representing the data received and address
        is the address of the socket sending the data
    """

    try:
        bytes_data, address = sock.recvfrom(data_chunk_size)
        return bytes_data, address
    except Exception:
        error_frame_summary = get_error_frame_summary()
        raise ReceiveFromFailure(error_frame_summary)


def send_client_data_back(sock: socket,
                          bytes_data: bytes,
                          address: Any) -> int:
    """
    Send data to the socket.

    :param sock: socket object
    :param bytes_data: bytes object
    :param address: address of the socket sending the data
    :return: number of bytes sent
    """

    try:
        bytes_sent = sock.sendto(bytes_data, address)
        return bytes_sent
    except Exception:
        error_frame_summary = get_error_frame_summary()
        raise SendToFailure(address, error_frame_summary)

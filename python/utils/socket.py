from socket import socket, AF_INET, SOCK_DGRAM as UDP


def create_socket(config):
    """Create and bind a UDP socket based on the provided configuration."""
    sock = socket(AF_INET, UDP)
    sock.bind((config.ip_address, config.port))
    return sock

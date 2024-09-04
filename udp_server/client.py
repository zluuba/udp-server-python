import socket

import constants as c
from errors.error_handler import handle_errors


def construct_tlv_packet(tag: bytes, value: str) -> bytes:
    tag_number = int(tag, 16)
    tag_bytes = tag_number.to_bytes(4)

    value_bytes = value.encode()
    length_bytes = len(value_bytes).to_bytes(4)

    return tag_bytes + length_bytes + value_bytes


def udp_client(server_ip, server_port, tlv_packet, timeout=1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(timeout)

    try:
        print(f'Sending message: {tlv_packet}')
        client_socket.sendto(tlv_packet, (server_ip, server_port))

        try:
            data, server = client_socket.recvfrom(c.DEFAULT_MTU)
            print(f"Received response: {data}")
        except socket.timeout:
            print("No response received.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()


@handle_errors
def main():
    server_ip = c.DEFAULT_IP_ADDRESS
    server_port = c.DEFAULT_PORT

    while True:
        tag = bytes(input('Enter command tag: ').encode())
        value = input('Enter command value: ')

        try:
            tlv_packet = construct_tlv_packet(tag, value)
            udp_client(server_ip, server_port, tlv_packet)
        except Exception:
            print('Tag should be a hex num only.')

        print()


if __name__ == "__main__":
    main()

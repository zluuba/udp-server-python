import socket
import constants as c


"""
This module is just a sandbox, forgive its ugliness
"""


def construct_tlv_packet(tag: int, value: str) -> bytes:
    tag_bytes = tag.to_bytes(4, byteorder='big')

    value_bytes = value.encode('utf-8')
    length_bytes = len(value_bytes).to_bytes(4, byteorder='big')

    tlv_packet = tag_bytes + length_bytes + value_bytes
    return tlv_packet


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


if __name__ == "__main__":
    server_ip = c.DEFAULT_IP_ADDRESS
    server_port = c.DEFAULT_PORT

    while True:
        tag = input('Enter command tag: ')
        value = input('Enter command value: ')

        try:
            if tag.startswith('0x'):
                hex_string = tag[2:]
                integer_value = int(hex_string, 16)
            else:
                raise ValueError('Tag should be represent as Hex number.')

            tlv_packet = construct_tlv_packet(integer_value, value)
            udp_client(server_ip, server_port, tlv_packet)
        except Exception as e:
            print('Cannot create TLV packet:', e)

        is_continue = input('Press Y to continue: ').lower()
        if is_continue != 'y':
            break

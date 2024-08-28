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

    # tag1 = 0x0
    # value1 = "1"
    #
    # print(f'Correct AmplifierSupplyCmd command sent: tag: {tag1}, value: {value1}')
    # tlv_packet1 = construct_tlv_packet(tag1, value1)
    # udp_client(server_ip, server_port, tlv_packet1)
    # print()

    # tag2 = 0x1
    # value2 = "dddeee"
    #
    # print(f'Correct NetworkTagCmd command sent: tag: {tag2}, value: {value2}')
    # tlv_packet2 = construct_tlv_packet(tag2, value2)
    # udp_client(server_ip, server_port, tlv_packet2)
    # print()

    # print(f'Two correct commands sent: tag1: {tag1}, value1: {value1}; tag2: {tag2}, value2: {value2}')
    # udp_client(server_ip, server_port, tlv_packet1 + tlv_packet2)
    # print()

    # tag3 = 0x3
    # value3 = "1"
    #
    # print(f'Incorrect command tag: tag: {tag3}, value: {value3}')
    # tlv_packet3 = construct_tlv_packet(tag3, value3)
    # udp_client(server_ip, server_port, tlv_packet3)
    # print()

    # tag4 = 0x0
    # value4 = "3"
    #
    # print(f'Incorrect AmplifierSupplyCmd command value: tag: {tag4}, value: {value4}')
    # tlv_packet4 = construct_tlv_packet(tag4, value4)
    # udp_client(server_ip, server_port, tlv_packet4)
    # print()

    # tag5 = 0x1
    # value5 = ("sjf'adbj'v'sdjbv'sebv'bjr'vaejf'sjkef"
    #           "ksjef'kes'fjsekf'fkvkjfkvbskfv;kjsebkrbvksebrbv"
    #           "jbb'vjsebv'ksebvbse'kbvksev'kbsek'vbsk'ebvksbe;vkjsev"
    #           "sjevjk'sbekvbs'ejkfbvk'sebfv'kjsbjfvksbefvjkbse"
    #           "jkabv'ksbevkbskvbs'kefkvsekfvsebf'abva"
    #           "fvnklnvsevsbvs;befkv;jebkvbjskfbvksb")
    #
    # print(f'Incorrect NetworkTagCmd command value: tag: {tag5}, value: {value5}')
    # tlv_packet5 = construct_tlv_packet(tag5, value5)
    # udp_client(server_ip, server_port, tlv_packet5)
    # print()

    # incorrect_packet = b'fnfnfnfnfnfnfn'
    #
    # print(f'Incorrect packet: {incorrect_packet}')
    # udp_client(server_ip, server_port, incorrect_packet)
    # print()

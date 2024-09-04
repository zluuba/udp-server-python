from unittest import TestCase, main

from udp_server.protocols.tlv import TLVPacket, parse_binary_data


DATA = {
    'cmd1': {
        'tag': '0x0',
        'length': 1,
        'value': '1',
        'binary': b'\x00\x00\x00\x00\x00\x00\x00\x011',
    },
    'cmd2': {
        'tag': '0x1',
        'length': 2,
        'value': '42',
        'binary': b'\x00\x00\x00\x01\x00\x00\x00\x0242',
    },
    'no_tlv': {
        'binary': b'qwertyqwertyqwerty',
        'errors': ['Incorrect TLV scheme: Invalid length field: 1954115959'],
    }
}


class TestServer(TestCase):
    def test_tlv_packet_parse(self):
        cmd = DATA['cmd1']
        tlv_packets, errors = parse_binary_data(cmd['binary'])
        tlv_packet = tlv_packets[0]
        actual_tlv_packet = TLVPacket(cmd['tag'], cmd['length'], cmd['value'])

        self.assertEqual(tlv_packet.tag, actual_tlv_packet.tag)
        self.assertEqual(tlv_packet.length, actual_tlv_packet.length)
        self.assertEqual(tlv_packet.value, actual_tlv_packet.value)
        self.assertEqual(errors, [])

    def test_tlv_packet_parse_mid_case(self):
        cmd1 = DATA['cmd1']
        cmd2 = DATA['cmd2']
        cmd3 = DATA['no_tlv']

        multy_tlv = cmd1['binary'] + cmd2['binary'] + cmd3['binary']
        tlv_packets, errors = parse_binary_data(multy_tlv)

        self.assertEqual(len(tlv_packets), 2)
        self.assertEqual(errors, cmd3['errors'])

    def test_no_tlv_packet_parse(self):
        cmd = DATA['no_tlv']
        tlv_packets, errors = parse_binary_data(cmd['binary'])

        self.assertEqual(tlv_packets, [])
        self.assertEqual(errors, cmd['errors'])


if __name__ == '__main__':
    main()

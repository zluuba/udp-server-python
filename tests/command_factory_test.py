from unittest import TestCase, main

from udp_server.commands.command_factory import command_factory
from udp_server.commands.valid_commands.amplifier_supply import AmplifierSupplyCmd
from udp_server.commands.invalid_commands.unknown import UnknownCmd
from udp_server.commands.invalid_commands.invalid import InvalidCmd
from udp_server.protocols.tlv import TLVPacket


DATA = {
    'cmd': {
        'tag': '0x0',
        'length': 1,
        'value': '1',
        'class': AmplifierSupplyCmd,
    },
    'unknown_cmd': {
        'tag': '0x3',
        'length': 1,
        'value': '1',
        'class': UnknownCmd,
    },
    'invalid_cmd': {
        'tag': '0x0',
        'length': 1,
        'value': '6',
        'class': InvalidCmd,
    },
}


class TestCommandFactory(TestCase):
    def test_command_factory(self):
        cmd = DATA['cmd']
        tlv_packet = TLVPacket(cmd['tag'], cmd['length'], cmd['value'])
        command = command_factory(tlv_packet)

        self.assertEqual(type(command), cmd['class'])
        self.assertTrue(command.validate())

    def test_command_factory_unknown_cmd(self):
        cmd = DATA['unknown_cmd']
        tlv_packet = TLVPacket(cmd['tag'], cmd['length'], cmd['value'])
        command = command_factory(tlv_packet)

        self.assertEqual(type(command), cmd['class'])
        self.assertFalse(command.validate())

    def test_command_factory_invalid_cmd(self):
        cmd = DATA['invalid_cmd']
        tlv_packet = TLVPacket(cmd['tag'], cmd['length'], cmd['value'])
        command = command_factory(tlv_packet)

        self.assertEqual(type(command), cmd['class'])
        self.assertFalse(command.validate())


if __name__ == '__main__':
    main()

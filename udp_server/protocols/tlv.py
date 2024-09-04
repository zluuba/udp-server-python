from struct import unpack, error as struct_error
from constants import UNPACK_FMT, TL_BYTES


class TLVPacket:
    def __init__(self, tag: str, length: int, value: str):
        self.tag = tag
        self.length = length
        self.value = value


def parse_binary_data(data: bytes) -> tuple[list, list]:
    """
    Parse binary data into TLV packets.

    :param data: binary data
    :return: tuple with (list[TLVPacket], list[error])
    """

    tlv_packets = []
    errors = []

    while data:
        try:
            tag, length = unpack(UNPACK_FMT, data[:TL_BYTES])
            value = data[TL_BYTES:TL_BYTES + length]

            tlv_packet = TLVPacket(tag, length, value)
            tlv_packets.append(tlv_packet)

            data = data[TL_BYTES + length:]

        except (struct_error, UnicodeDecodeError) as e:
            error = f'Incorrect TLV scheme: {e}'
            errors.append(error)
            break

    return tlv_packets, errors

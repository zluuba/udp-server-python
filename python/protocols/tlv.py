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

    Args:
        data (bytes): The raw binary data to be parsed.

    Returns:
        tuple: A tuple containing two elements:
            - A list of TLVPacket objects parsed from the data.
            - A list of error messages encountered during parsing.

    Raises:
        ValueError: If the length field is invalid.
        struct_error: If unpacking the data fails.
        UnicodeDecodeError: If decoding the value field fails.
    """

    tlv_packets = []
    errors = []

    while data:
        try:
            tag, length = unpack(UNPACK_FMT, data[:TL_BYTES])

            if not (0 < length <= len(data) - TL_BYTES):
                raise ValueError(f'Invalid length field: {length}')

            value = data[TL_BYTES:TL_BYTES + length].decode('utf-8')

            tlv_packet = TLVPacket(hex(tag), length, value)
            tlv_packets.append(tlv_packet)

            data = data[TL_BYTES + length:]

        except (struct_error, UnicodeDecodeError, ValueError) as e:
            error = f'Incorrect TLV scheme: {e}'
            errors.append(error)
            break

    return tlv_packets, errors

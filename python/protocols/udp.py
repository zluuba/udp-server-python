from protocols.tlv import parse_binary_data


class UdpPacket:
    def __init__(self, raw_data):
        self.__raw_data = raw_data
        self.__data = []
        self.__errors = []

    @property
    def data(self):
        """Returns a list of valid TLV packets."""
        if not self.__data and not self.__errors:
            self._process_raw_data()

        return self.__data

    def _process_raw_data(self):
        """Process the raw binary data and parse it into TLV packets."""
        data, errors = parse_binary_data(self.__raw_data)
        self.__errors.extend(errors)
        self.__data = data

    @property
    def errors(self):
        return self.__errors

DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 31337
DEFAULT_MTU = 1500
DEFAULT_HANDLED_PROTOCOL = 'TLV'

# Format for 'unpack' function
# '!' - network byte order, 'I' - unsigned int of size 4
UNPACK_FMT = '!II'

# 4 bytes for tag, 4 bytes for length (TLV)
TL_BYTES = 8

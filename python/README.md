# TLV UDP Server (Python)

- simple and readable
- single-threaded, blocking I/O
- about 80% complete
- includes client part
- contains some tests (< 50%)


### Thoughts

- `server.py` - entry point. plain written, but maintainable in parts (by commands in general).
- `config` placed for future maintenance, it allows for expansion to other ports and IPs.
- `UdpPacket` handles the logical part of a large data packet, containing only TLV chunks and main errors that may appear while parsing TLV chunks.
- `commands` are the most thoughtfully designed. Included:
  - `command_factory` for easy command creation.
  - `valid_commands/` for quick maintenance.
  - `invalid_commands/` for handling invalid data similarly to commands, but with some restrictions.
  - `commands map` is just for collecting all valid commands in one place
- `protocols/` is an artifact of the idea that a server with fully flexible configuration is a good idea. This should include the ability to choose between UDP or TCP and select from various known protocol schemas to parse data.


### Usage
To run the server, type `python3 server.py`. To run the client, use `python3 client.py` (or use netcat/nc).  
Python3 must be installed.
  
Some data for testing:

```commandline
# valid. tag: 0x0, value: 1
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x011' | nc -u -w1 127.0.0.1 31337

# valid. tag: 0x1, value: 42
echo -ne '\x00\x00\x00\x01\x00\x00\x00\x0242' | nc -u -w1 127.0.0.1 31337

# two valid commands
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x011\x00\x00\x00\x01\x00\x00\x00\x0242' | nc -u -w1 127.0.0.1 31337

# unknown tag. tag: 0x3, value: 0
echo -ne '\x00\x00\x00\x03\x00\x00\x00\x010' | nc -u -w1 127.0.0.1 31337

# invalid value. tag: 0x0, value: 8
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x018' | nc -u -w1 127.0.0.1 31337

# no TLV found
echo -ne 'linuswouldbescreamingifhesawthiscode' | nc -u -w1 127.0.0.1 31337
```
  
# UDP Server for TLV Packets (Rust)

- it works, but unreadable
- about 50% complete


### Thoughts

- reference structure: code in Python
- have magic numbers
- 13 warnings emitted


### Usage
Not intended for use.  
To run the server, type `cargo run`. To run the client, use netcat/nc.  
Rust must be installed.
  
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

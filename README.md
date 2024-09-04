# Simple UDP Server (Python)

Simple UDP server that can receive TLV-scheme data with a bunch of commands.  
Single-threaded, blocking I/O (for now).


### Requirements
You only need to have [Python](https://www.python.org/) installed (version 3.11 or higher).  
You can download it [here](https://www.python.org/downloads/).


### Installation / Running
Open a terminal window. 
Clone this repository (with [Git](https://git-scm.com/downloads)) or download it with [Pip](https://pip.pypa.io/en/stable/installation/):
```bash
git clone https://github.com/zluuba/udp_tlv_server.git
```
```bash
pip install --user git+https://github.com/zluuba/udp_tlv_server.git
```

Navigate to the `udp_tlv_server/python`:
```bash
cd udp_tlv_server/python
```

Run the server:
```bash
make server
```

Run the client (or use netcat/nc):
```bash
make client
```

  
### Testing
Data for testing

```commandline
# valid. tag: 0x0, value: 1
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x011' | nc -u -w1 127.0.0.1 31337

# valid. tag: 0x1, value: 42
echo -ne '\x00\x00\x00\x01\x00\x00\x00\x0242' | nc -u -w1 127.0.0.1 31337

# two commands: valid
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x011\x00\x00\x00\x01\x00\x00\x00\x0242' | nc -u -w1 127.0.0.1 31337

# two commands: valid and invalid
echo -ne '\x00\x00\x00\x01\x00\x00\x00\x0242\x00\x00\x00\x00\x00\x00\x00\x018' | nc -u -w1 127.0.0.1 31337

# invalid command: unknown tag. tag: 0x3, value: 0
echo -ne '\x00\x00\x00\x03\x00\x00\x00\x010' | nc -u -w1 127.0.0.1 31337

# invalid command: invalid value. tag: 0x0, value: 8
echo -ne '\x00\x00\x00\x00\x00\x00\x00\x018' | nc -u -w1 127.0.0.1 31337

# incorrect TLV scheme
echo -ne 'linuswouldbescreamingifhesawthis' | nc -u -w1 127.0.0.1 31337
```
  

### Additional
You can check project with tests, linter and typing checker.  
You need `pytest`, `flake8` and `mypy` to be installed 
(better be installing them in [venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments)):
```bash
make install-dev-dep
```


To run all checks (tests, linter, typing checks, test coverage) run the following command:
```bash
make check
```

Or run checks separately:
```bash
make test
make lint
make typing
make test-coverage
```

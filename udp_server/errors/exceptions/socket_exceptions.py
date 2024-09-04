from traceback import FrameSummary
from typing import Any


class AddressAlreadyInUse(Exception):
    """
    Raised when socket cannot be opened
    because address already in use.
    """

    def __init__(self, ip_address: str, port: int,
                 error_frame: FrameSummary):

        self.ip_address = ip_address
        self.port = port
        self.error_frame = error_frame

        super().__init__(f"Can\'t open socket on "
                         f"{self.ip_address}:{self.port}. "
                         f"Address already in use. "
                         f"Error location: {self.error_frame.filename}.")


class ReceiveFromFailure(Exception):
    """
    Raised when an error occurred while
    receiving data from socket.
    """

    def __init__(self, error_frame: FrameSummary):
        self.error_frame = error_frame

        super().__init__(f"Can\'t receive data from socket. "
                         f"Error location: {self.error_frame.filename}.")


class SendToFailure(Exception):
    """
    Raised when an error occurred while
    sending data to the socket.
    """

    def __init__(self, address: Any, error_frame: FrameSummary):
        self.address = address
        self.error_frame = error_frame

        super().__init__(f"Can\'t send data to {self.address}. "
                         f"Error location: {self.error_frame.filename}.")

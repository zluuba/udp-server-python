from dataclasses import dataclass
import constants as c


@dataclass
class Config:
    ip_address: str = c.DEFAULT_IP_ADDRESS
    port: int = c.DEFAULT_PORT
    mtu: int = c.DEFAULT_MTU
    handled_protocol: str = c.DEFAULT_HANDLED_PROTOCOL

    def update_config(self, **kwargs):
        """
        Stub. Future functionality:
        Update the configuration data using the provided keyword arguments.
        This method can update the entire configuration or specific fields.
        """
        pass

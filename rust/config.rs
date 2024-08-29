use crate::constants::{IP_ADDRESS, PORT, MTU};

pub struct Config {
    pub ip_address: String,
    pub port: u16,
    pub mtu: u16,
}

impl Config {
    pub fn new() -> Self {
        Config {
            ip_address: IP_ADDRESS.to_string(),
            port: PORT,
            mtu: MTU,
        }
    }
}

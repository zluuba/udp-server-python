use std::net::UdpSocket;
use crate::config::Config;
use crate::tlv::parse_tlv;
use crate::commands::command_factory::command_factory;

pub fn run() -> std::io::Result<()> {
    {
        let config = Config::new();
        let address = format!("{}:{}", config.ip_address, config.port);
        let socket = UdpSocket::bind(&address)?;
        let mut buf = vec![0u8; config.mtu as usize];

        loop {
            let (data, src) = socket.recv_from(&mut buf)?;
            let (tlv_packets, errors) = parse_tlv(&buf[..data]);

            for packet in tlv_packets {
                let string_value = String::from_utf8(packet.value).unwrap();
                let command = command_factory(packet.tag, string_value);

                if !command.validate() {
                    continue;
                }

                eprintln!("Operation '{}' was successfully completed.", command.name());
            }

            if !errors.is_empty() {
                eprintln!("UDP Packet has errors: {:?}", errors)
            } else {
                socket.send_to(&buf[..data], &src)?;
            }
        }
    }
    Ok(())
}

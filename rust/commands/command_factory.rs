use crate::commands::valid_commands::amplifier_supply::AmplifierSupplyCmd;
use crate::commands::valid_commands::network_tag::NetworkTagCmd;
use crate::commands::invalid_commands::{UnknownCmd, InvalidCmd};


pub enum Command {
    AmplifierSupply(AmplifierSupplyCmd),
    NetworkTag(NetworkTagCmd),
    Unknown(UnknownCmd),
    Invalid(InvalidCmd),
}

impl Command {
    pub fn validate(&self) -> bool {
        match self {
            Command::AmplifierSupply(cmd) => cmd.validate(),
            Command::NetworkTag(cmd) => cmd.validate(),
            Command::Unknown(cmd) => cmd.validate(),
            Command::Invalid(cmd) => cmd.validate(),
        }
    }

    pub fn name(&self) -> &str {
        match self {
            Command::AmplifierSupply(cmd) => cmd.name(),
            Command::NetworkTag(cmd) => cmd.name(),
            Command::Unknown(cmd) => "Unknown Command",
            Command::Invalid(cmd) => "Invalid Command",
        }
    }
}

pub fn command_factory(tag: u32, value: String) -> Command {
    let tag_str = format!("0x{:X}", tag);

    match tag_str.as_str() {
        "0x0" => {
            let cmd = AmplifierSupplyCmd::new(value.clone());

            if cmd.validate() {
                Command::AmplifierSupply(cmd)
            } else {
                Command::Invalid(InvalidCmd { tag: tag_str, value })
            }
        },
        "0x1" => {
            let cmd = NetworkTagCmd::new(value.clone());

            if cmd.validate() {
                Command::NetworkTag(cmd)
            } else {
                Command::Invalid(InvalidCmd { tag: tag_str, value })
            }
        },
        _ => Command::Unknown(UnknownCmd { tag: tag_str, value }),
    }
}
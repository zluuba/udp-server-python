mod constants;
mod config;
mod server;
mod tlv;
mod commands;

fn main() -> std::io::Result<()> {
    server::run()
}

pub struct TLVPacket {
    pub tag: u32,
    pub length: u32,
    pub value: Vec<u8>,
}

#[derive(Debug)]
pub struct TLVError {
    pub index: usize,
    pub message: String,
}

pub fn parse_tlv(data: &[u8]) -> (Vec<TLVPacket>, Vec<TLVError>) {
    let mut packets = Vec::new();
    let mut errors = Vec::new();
    let mut index = 0;

    while index + 8 <= data.len() {
        let tag = u32::from_be_bytes([data[index], data[index + 1], data[index + 2], data[index + 3]]);
        index += 4;

        let length = u32::from_be_bytes([data[index], data[index + 1], data[index + 2], data[index + 3]]);
        index += 4;

        if index + length as usize > data.len() {
            errors.push(TLVError {
                index,
                message: format!("Incorrect TLV schema. Expected length: {}, available: {}", length, data.len() - index),
            });
            break;
        }

        let value = data[index..index + length as usize].to_vec();
        index += length as usize;

        packets.push(TLVPacket { tag, length, value });
    }

    return (packets, errors)
}

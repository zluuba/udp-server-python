const TAG: &str = "0x1";
const NAME: &str = "метка сети";
const MAX_BYTES: usize = 255;

pub struct NetworkTagCmd {
    pub value: String,
}

impl NetworkTagCmd {
    pub fn new(value: String) -> Self {
        NetworkTagCmd { value }
    }

    pub fn validate(&self) -> bool {
        self.value.len() <= MAX_BYTES
    }

    pub fn name(&self) -> &str {
        NAME
    }

    pub fn tag(&self) -> &str {
        TAG
    }
}
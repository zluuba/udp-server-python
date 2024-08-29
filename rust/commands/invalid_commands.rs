pub struct UnknownCmd {
    pub tag: String,
    pub value: String,
}

impl UnknownCmd {
    pub fn validate(&self) -> bool {
        false
    }

    pub fn name(&self) -> &str {
        "Unknown"
    }
}

pub struct InvalidCmd {
    pub tag: String,
    pub value: String,
}

impl InvalidCmd {
    pub fn validate(&self) -> bool {
        false
    }

    pub fn name(&self) -> &str {
        "InvalidCmd"
    }
}
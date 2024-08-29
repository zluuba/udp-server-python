const TAG: &str = "0x0";
const NAME: &str = "питание усилителя";
const ALLOWED_VALUES: [&str; 2] = ["0", "1"];

pub struct AmplifierSupplyCmd {
    pub value: String,
}

impl AmplifierSupplyCmd {
    pub fn new(value: String) -> Self {
        AmplifierSupplyCmd { value }
    }

    pub fn validate(&self) -> bool {
        ALLOWED_VALUES.contains(&self.value.as_str())
    }

    pub fn name(&self) -> &str {
        NAME
    }

    pub fn tag(&self) -> &str {
        TAG
    }
}
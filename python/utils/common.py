def are_commands_valid(commands):
    """Check the validity of all commands in a UDP packet."""
    return all(command.validate() for command in commands)

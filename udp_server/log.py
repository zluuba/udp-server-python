from sys import stderr


MESSAGES = {
    'run_command': lambda name: f'Operation "{name}" '
                                f'was successfully completed.\n',
    'udp_errors': lambda udp: f'UDP Packet has errors: {", ".join(udp.errors)}.\n'
}


def write(action, args_dict):
    log_message_func = MESSAGES.get(action)

    if log_message_func:
        log_message = log_message_func(args_dict)
        stderr.write(log_message)

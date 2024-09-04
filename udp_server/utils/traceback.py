from traceback import extract_stack, FrameSummary


def get_error_frame_summary() -> FrameSummary:
    """
    Extract the raw traceback from the current stack frame and
    return frame where error was raised:
        [-1] - current function,
        [-2] - previous function where error was occurred.

    :return: FrameSummary with full info about error location
    """

    traceback_stack = extract_stack()
    return traceback_stack[-2]

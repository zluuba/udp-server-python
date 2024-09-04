from functools import wraps
from sys import stderr, exit

from utils.socket import close_socket


def handle_errors(func):
    """
    Handle all app errors:
        - while Ctrl+C pressed (KeyboardInterrupt), it supress traceback
          and quietly exit the process
        - while any other error occurred, writing log in stderr
          and exit the process with error

    Closes socket in any case.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyboardInterrupt:
            exit(0)
        except Exception as error:
            stderr.write(str(error))
            exit(1)
        finally:
            _, sock = args
            close_socket(sock)

    return wrapper

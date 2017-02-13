#!/usr/bin/env python
from __future__ import print_function
import signal
import requests

class TimeoutException(Exception):
    """
    Exception called on timeouts.
    """
    pass

def requestTimeout(signum, frame):
    """
    Request timeout.
    """

    raise TimeoutException()

def do(hostname):
    """
    Performs a GET request.

    Parameters
    ----------
    hostname : str
        Target request

    Return
    ------
    The request results
    """

    try:
        return requests.get(hostname, timeout=10)

    except TimeoutException:
        print("\033[1;31mRequest timeout: test aborted\n\033[1;m")
        return None

    except requests.ConnectionError:
        print("\033[1;31mServer not found: test aborted\n\033[1;m")
        return None

    finally:
        signal.alarm(0)

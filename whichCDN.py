#!/usr/bin/env python
from __future__ import print_function
import argparse
import signal
import sys

from utils import loader
from utils import request

if sys.version_info >= (3, 0):
    import urllib.parse as urlparse
else:
    import urlparse


def parser():
    """Parse arguments."""

    parser = argparse.ArgumentParser(description="""\
        WhichCDN allows to detect if a given website is protected by a Content
        Delivery Network.\r Fell free to contact the maintainer for any further
        questions or improvement vectors.\r Maintained by Nitrax
        <nitrax@lokisec.fr>
    """)

    parser.add_argument('target', type=str, help='hostname to scan')

    parser.parse_args()


def sanitizeURL(hostname):
    """Sanitizes the hostname by adding the http protocol if it has not been
    provided.

    Parameters
    ----------
    hostname : str
        Hostname to assess

    Return
    ------
    The hostname sanitized
    """

    components = urlparse.urlparse(hostname)

    hostname = "http://" + hostname if components.scheme == '' else hostname
    return hostname


if __name__ == "__main__":

    print("""
     __      __.__    .__       .__    _________ ________    _______
    /  \    /  \  |__ |__| ____ |  |__ \_   ___ \\\\______ \   \      \\
    \   \/\/   /  |  \|  |/ ___\|  |  \/    \  \/ |    |  \  /   |   \\
     \        /|   Y  \  \  \___|   Y  \     \____|    `   \/    |    \\
      \__/\  / |___|  /__|\___  >___|  /\______  /_______  /\____|__  /
           \/       \/        \/     \/        \/        \/         \/
    """)

    parser()

    signal.signal(signal.SIGALRM, request.requestTimeout)
    signal.alarm(5)

    hostname = sanitizeURL(sys.argv[1])

    for module in loader.getPlugins():
        plugin = loader.loadPlugin(module)
        plugin.detect(hostname)

    print('\033[1;31mNo CDN found\033[1;m')

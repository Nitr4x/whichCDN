#!/usr/bin/env python

from __future__ import print_function
import sys
from utils import CDNEngine

if sys.version_info >= (3, 0):
    import subprocess as commands
    import urllib.parse as urlparse
else:
    import commands
    import urlparse

def detect(hostname):
    """
    Performs CDN detection through whois command's.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print('[+] Whois detection\n')

    hostname = urlparse.urlparse(hostname).netloc

    out = commands.getoutput("whois " + hostname)

    CDNEngine.find(out.lower())

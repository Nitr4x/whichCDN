#!/usr/bin/env python

from __future__ import print_function
import sys
import re
from utils import CDNEngine

if sys.version_info >= (3, 0):
    import subprocess as commands
    import urllib.parse as urlparse
else:
    import commands
    import urlparse

def detect(hostname):
    """
    Performs CDN detection through the DNS, using the nslookup command.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print('[+] DNS detection\n')

    hostname = urlparse.urlparse(hostname).netloc
    regexp = re.compile('\\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\b')

    out = commands.getoutput("host " + hostname)
    addresses = regexp.finditer(out)

    for addr in addresses:
        CDNEngine.find(commands.getoutput('nslookup ' + addr.group()))

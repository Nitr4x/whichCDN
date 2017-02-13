#!/usr/bin/env python

from __future__ import print_function
import sys
import re
from utils import CDNEngine
from utils import request

if sys.version_info >= (3, 0):
    import subprocess as commands
    import urllib.parse as urlparse
else:
    import commands
    import urlparse

def detect(hostname):
    """
    Performs CDN detection thanks to information disclosure from server error.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print('[+] Error server detection\n')

    hostname = urlparse.urlparse(hostname).netloc
    regexp = re.compile('\\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\b')

    out = commands.getoutput("host " + hostname)
    addresses = regexp.finditer(out)

    for addr in addresses:
        res = request.do('http://' + addr.group())
        if res is not None and res.status_code == 500:
            CDNEngine.find(res.text.lower())

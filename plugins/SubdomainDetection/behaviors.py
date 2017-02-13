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
    Performs CDN detection by trying to access the cdn subdomain of the
    specified hostname.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print('[+] CDN subdomain detection\n')

    hostname = "cdn." + urlparse.urlparse(hostname).netloc

    out = commands.getoutput("host -a " + hostname)

    CDNEngine.find(out.lower())

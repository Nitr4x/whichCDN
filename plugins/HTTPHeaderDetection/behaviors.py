#!/usr/bin/env python
from __future__ import print_function
import sys
from utils import CDNEngine
from utils import request

if sys.version_info >= (3, 0):
    import urllib.parse as urlparse
else:
    import urlparse


def detect(hostname):
    """
    Performs CDN detection thanks to HTTP headers.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print('[+] HTTP header detection\n')

    hostname = urlparse.urlparse(hostname).scheme + '://' + urlparse.urlparse(hostname).netloc

    fields = {
        'Server': True,
        'X-CDN': True,
        'x-cache': True,
        'X-CDN-Forward': True,
        'Fastly-Debug-Digest': False
    }

    res = request.do(hostname)

    if res is None:
        return

    for field, state in fields.items():
        value = res.headers.get(field)
        if state and value is not None:
            CDNEngine.find(value.lower())
        elif not state and value is not None:
            CDNEngine.find(field.lower())

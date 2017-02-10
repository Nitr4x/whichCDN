import sys
import urlparse

from utils import CDNEngine
from utils import request

def detect(hostname):
    """Performs CDN detection thanks to HTTP headers.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print '[+] HTTP header detection\n'

    hostname = urlparse.urlparse(hostname).scheme + '://' + urlparse.urlparse(hostname).netloc

    fields = {
        'Server': True,
        'X-CDN': True,
        'x-cache': True,
        'X-CDN-Forward': True,
        'Fastly-Debug-Digest': False
    }

    res = request.do(hostname)

    if res == None:
        return

    for field, state in fields.items():
        value = res.headers.get(field)
        if state and value != None:
            CDNEngine.find(value.lower())
        elif not state and value != None:
            CDNEngine.find(field.lower())

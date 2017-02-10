import commands
import urlparse

from utils import CDNEngine

def detect(hostname):
    """Performs CDN detection by trying to access the cdn subdomain of the
    specified hostname.

    Parameters
    ----------
    hostname : str
        Hostname to assess
    """

    print '[+] CDN subdomain detection\n'

    hostname = "cdn." + urlparse.urlparse(hostname).netloc

    out = commands.getoutput("host -a " + hostname)

    CDNEngine.find(out.lower())

import commands
import urlparse

from utils import CDNEngine

def detect(hostname):
    print '[+] CDN subdomain detection\n'

    hostname = "cdn." + urlparse.urlparse(hostname).netloc

    out = commands.getoutput("host -a " + hostname)

    CDNEngine.find(out.lower())

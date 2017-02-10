import commands
import sys
import urlparse
import re

from utils import CDNEngine

def detect(hostname):
    print '[+] DNS detection\n'

    hostname = urlparse.urlparse(hostname).netloc
    regexp = re.compile('\\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\b')

    out = commands.getoutput("host " + hostname)
    addresses = regexp.finditer(out)

    for addr in addresses:
        CDNEngine.find(commands.getoutput('nslookup ' + addr.group()))

import commands
import re
import sys
import urlparse

import CDNEngine
import request

def detect(hostname):
    print '[+] Error server detection\n'

    hostname = urlparse.urlparse(hostname).netloc
    regexp = re.compile('\\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\\b')

    out = commands.getoutput("host " + hostname)
    addresses = regexp.finditer(out)

    for addr in addresses:
        res = request.do('http://' + addr.group())
        if res != None and res.status_code == 500:
            CDNEngine.find(res.text.lower())

"""DNSDetection plugin performs CDN detection through nslookup results."""

import sys

sys.path.insert(0, 'plugins/')

from DNSDetection.behaviors import detect

sys.path.pop(0)

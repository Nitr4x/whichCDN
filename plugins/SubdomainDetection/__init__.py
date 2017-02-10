"""CDN are, sometimes, deployed on a specific subdomain. SubdomainDetection
plugin performs CDN detection by trying to access this specific subdomain and
by analyzing its DNS.
"""

import sys

sys.path.insert(0, 'plugins/')

from SubdomainDetection.behaviors import detect

sys.path.pop(0)

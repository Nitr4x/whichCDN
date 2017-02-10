"""ErrorServerDetection plugin performs CDN detection when attempts to access 
the web server via its IP address fail and disclose information about
the CDN in place.
"""

import sys

sys.path.insert(0, 'plugins/')

from ErrorServerDetection.behaviors import detect

sys.path.pop(0)

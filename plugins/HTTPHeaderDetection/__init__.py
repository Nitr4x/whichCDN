"""HTTPHeaderDetection plugin performs CDN detection by assessing HTTP headers."""

import sys

sys.path.insert(0, 'plugins/')

from HTTPHeaderDetection.behaviors import detect

sys.path.pop(0)

#!/usr/bin/env python
"""
ErrorServerDetection plugin performs CDN detection when attempts to access
the web server via its IP address fail and disclose information about
the CDN in place.
"""

from plugins.ErrorServerDetection.behaviors import detect

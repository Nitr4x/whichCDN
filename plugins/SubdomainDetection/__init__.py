#!/usr/bin/env python
"""
CDN are, sometimes, deployed on a specific subdomain. SubdomainDetection
plugin performs CDN detection by trying to access this specific subdomain and
by analyzing its DNS.
"""

from plugins.SubdomainDetection.behaviors import detect

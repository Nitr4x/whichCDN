import sys

CDN = {
    'Cloudflare': 'Cloudflare - https://www.cloudflare.com',
    'Incapsula': 'Incapsula - https://www.incapsula.com/',
    'Cloudfront': 'Cloudfront - https://aws.amazon.com/cloudfront/',
    'Akamai': 'Akamai - https://akamai.com',
    'Airee': 'Airee - https://airee.international',
    'CacheFly': 'CacheFly - https://www.cachefly.com/',
    'EdgeCast': 'EdgeCast - https://verizondigitalmedia.com',
    'MaxCDN': 'MaxCDN - https://www.maxcdn.com/',
    'Beluga': 'BelugaCDN - https://belugacdn.com',
    'Limelight': 'Limelight -  https://www.limelight.com',
    'Fastly': 'Fastly - https://www.fastly.com/',
    'Myracloud': 'Myra - https://myracloud.com',
    'msecnd.ne': 'Microsoft Azure - https://azure.microsoft.com/en-us/services/cdn/'
}

def find(data):
    """Compares the provided data to the CDN supported.

    Parameters
    ----------
    data : str
        Data to analyze
    """

    for keyword, description in CDN.items():
        if data.find(keyword.lower()) != -1:
            print '\033[1;32mCDN found: ' + description + '\033[1;m\n'
            sys.exit(0)

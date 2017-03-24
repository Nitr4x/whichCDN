#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name='whichCDN',
    version='1.0',
    description='WhichCDN allows to detect if a given website is protected by a Content Delivery Network',
    author_email='nitrax@lokisec.fr',
    author='Nitrax',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/Nitr4x/whichCDN',
    scripts=['whichCDN'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: MIT',
        'Operating system :: Unix',
        'Operating system :: Windows',
        'Operating system :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'requests'
    ]
)

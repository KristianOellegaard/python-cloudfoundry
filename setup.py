#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from cloudfoundry.version import version
from distutils.core import setup

setup(
    author=u'Kristian Øllegaard',
    author_email='kristian@oellegaard.com',
    name='python-cloudfoundry',
    description='Python interface to CloudFoundry',
    version=version,
    url='http://www.github.com/KristianOellegaard/python-cloudfoundry/',
    license='MIT License',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=[
        open("requirements.txt").readlines(),
    ],
)
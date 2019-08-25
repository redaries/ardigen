#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

from setuptools import setup, find_packages

setup(
    name="ardigen",
    url='https://github.com/redaries/ardigen.git',
    description='Ardigen',
    version="0.1.0",
    python_requires=">=3.4",
    install_requires=['pandas'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    license='Apache Software License',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'fizzbuzz=ardigen.fizzbuzz:main',
            'valuation=ardigen.valuation:main',
        ],
    },
)

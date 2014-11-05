#!/usr/bin/env python

import spate

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='spate',
    version=spate.__version__,
    description='Python spate client',
    author='Joe Alcorn',
    author_email='joe@gorealtime.io',
    url='https://spate.io',
    packages=find_packages(),
    package_data={
        'spate': ['README.md'],
        'spate.vendor.requests': ['*.pem'],
    },
    long_description=readme,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)

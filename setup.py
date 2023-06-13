#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ranktier
from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(name="ranktier",
    version=ranktier.__version__,
    description="A Dota rank tier converter",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/marcusmunch/ranktier",
    license="GPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
        ],
    author="Marcus Grünewald",
    author_email="marcus@marcusmunch.dk",
    packages=["ranktier"])

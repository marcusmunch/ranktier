# -*- coding:utf-8 -*-

from setuptools import setup

setup(name="ranktier",
	version="1.0",
	description="A Dota rank tier converter",
	long_description="Ranktier turns two-digit rank tier numbers into human-readable output.",
	url="https://github.com/marcusmunch/ranktier",
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: English",
		"Programming Language :: Python :: 2.7"],
	author="Marcus Grünewald",
	author_email="marcus@marcusmunch.dk",
	packages=["ranktier"])
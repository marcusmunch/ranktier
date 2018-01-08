ranktier
========
[![Build Status](https://travis-ci.org/marcusmunch/ranktier.svg?branch=master)](https://travis-ci.org/marcusmunch/ranktier)
[![PyPI](https://img.shields.io/pypi/v/ranktier.svg)](https://pypi.python.org/pypi/ranktier)
[![PyPI](https://img.shields.io/pypi/pyversions/ranktier.svg)](https://pypi.python.org/pypi/ranktier)
[![PyPI](https://img.shields.io/pypi/l/ranktier.svg)](https://pypi.python.org/pypi/ranktier)

ranktier converts `rank_tier` numbers from APIs like OpenDota to human-readable ranks

Setup
-----
`ranktier` can be installed from [PyPi](https://pypi.python.org/pypi):
`pip install ranktier`

It can also be installed by downloading the repo and running `pip install .`

Note that `ranktier` requires [requests](http://python-requests.org), but the installer knows this. 😁 

Usage
-----
`ranktier` has one function:
```python
>>> import ranktier
>>> rank = 42
>>> ranktier.ranktier(rank)
'Archon [2]'
```

`rank` has to be a two-digit number for ranktier to work. Ranktier works regardless of `rank` being a `str`-type or `int`-type variable.

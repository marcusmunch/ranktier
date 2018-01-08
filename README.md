ranktier
========
ranktier converts `rank_tier` numbers from APIs like OpenDota to human-readable ranks

Setup
-----
Currently, the module can only be installed by downloading the repository locally. From there, you can run
`python setup ranktier`.

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

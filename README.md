ranktier
========
ranktier converts `rank_tier` numbers from APIs like OpenDota to human-readable ranks

Setup
-----
Currently, the module can only be installed by downloading the repository locally. From there, you can run
`python setup ranktier`.

Usage
-----

```python
import ranktier

ranktier.ranktier(rank)
```

`rank` has to be a two-digit number to work. Ranktier works regardless of `rank` being a `str`-type or `int`-type variable.

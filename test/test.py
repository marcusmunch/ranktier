#!/usr/bin/env python
import sys

import ranktier

for n in [42, '42', 'null', 404]:
	r = ranktier.Rank(n)

	print(r)

for steamid in sys.argv[1:]:
	p = ranktier.Player(steamid)

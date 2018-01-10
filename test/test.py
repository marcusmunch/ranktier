#!/usr/bin/env python

import ranktier

for n in [42, '42', 'null', 404]:
	r = ranktier.Rank(n)

	print(r)
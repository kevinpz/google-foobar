#!/usr/bin/env python3

import sys
from math import sqrt

def answer(area):
	result = []
	remaining = area

	while remaining != 0:
		maxsize = int(sqrt(remaining))
		area = maxsize * maxsize
		result.append(area)
		remaining -= area

	print(result)

	return result

area = int(sys.argv[1])
answer(area)

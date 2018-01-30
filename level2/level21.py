#!/usr/bin/env python2
"""
We need to calculate the diff between each of the pegs
Let's say we have A, B, C, ..., M, N pegs
So we have:
AB = dAB
BC = dAC
...
MN = dMN

And let's say we have xA, xB, xC, ..., xM, xN the radius of each gears
So we have:
xA + xB = dAB
xB + xC = dBC
...
xM + xN = dMN

And as we want to have the last gear at twice the rate of the first one, we also have:
xN = xA / 2 => xN - xA / 2 = 0

So we can have something like :
xA + xB = dAB
xB + xC = dBC
...
xM + xN = dMN
xN - xA / 2 = 0

And with line combinaison:
Odd number of gears:
xA + xB - xB -xC + ... - xM - xN = dAB - dBC + ... - dMN
with simplification:
xA - xN = dAB - dBC + ... - dMN
xA - 1/2 xA = dAB - dBC + ... - dMN
xA = 2 * (dAB - dBC + ... - dMN)

Even number of gears:
xA + xB - xB -xC + ... + xM + xN = dAB - dBC + ... + dMN
with simplification:
xA + xN = dAB - dBC + ... + dMN
xA + 1/2 xA = dAB - dBC + ... + dMN
xA = 2 * (dAB - dBC + ... + dMN) / 3


"""

# Calculate the Greatest Common Divisor of a and b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculateFirstGear(pegs, space):
	add = space[0::2]
	rem = space[1::2]
	total = sum(add) - sum(rem)

	#odd case
	if (len(pegs) %2 == 1):
		num = 2 * total
		den = 1
		
	#even case
	else:
		num = 2 * total
		den = 3
		pgcd = gcd(num,den)
		num /= pgcd
		den /= pgcd

	result = [num, den]
	return result

def checkGearSize(pegs, space, result):
	lastValue = (float(result[0]) / float(result[1]))
	if (lastValue < 1):
		return False
	for i in xrange(0,len(space)):
		newValue = space[i] - lastValue
		if (newValue < 1):
			return False
		lastValue = newValue
	return True

def answer(pegs):
	space = [j - i for i,j in zip(pegs[:-1], pegs[1:])]
	result = calculateFirstGear(pegs, space)
	if not checkGearSize(pegs, space, result):
		result = [-1, -1]		
	print(result)
	return result


pegs = [4, 30, 50]
answer(pegs)

pegs = [4, 17, 50]
answer(pegs)

pegs = [2, 8, 11, 15, 20, 24]
answer(pegs)
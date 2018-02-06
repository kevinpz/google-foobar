#!/usr/bin/env python2
"""
Instead of starting with 1, 1 and try to reach the M, F number
We can start with M, F and try to reach the 1, 1 starting position
For each iteration, we choose the biggest number, and we substract it with the other one
This works well, but we low number.

To improve the process, we can use integer division, and modulo
We divide the biggest number with the other one to see how many steps it lasts
Then, we take the modulo to have the remaining number
"""

def answer(M, F):
	curM, curF = long(M), long(F)
	cpt = 0

	#while we still have or count superior to 1
	while curM > 1 and curF > 1:
		if curM > curF:
			#we see how step it lasts to multiplicate bombs
			cpt_add = curM / curF
			#and we set the remaining
			curM = curM % curF
		else:
			cpt_add = curF / curM
			curF = curF % curM

		#update the number of required step
		cpt += cpt_add

	#if we have a count lower than 1, it means it's impossible
	if curM < 1 or curF < 1:
		cpt = 'impossible'
	else:
		#we pick the remaining not 1 number
		my_max = max(curM, curF)
		#and add it to the count
		cpt = cpt + my_max - 1

	print(cpt)
	return cpt

answer(2, 1)
#1

answer(2, 4)
#impossible

answer(4, 7)
#4
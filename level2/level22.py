#!/usr/bin/env python2

def generousCase(total_lambs):
	remaining = total_lambs
	last = 0
	current = 1
	number = 0
	while (remaining >= current):
		remaining -= current
		number += 1
		last = current
		current *= 2

	#check if we can add a final one with the remaining lambs
	if(remaining >= last + last / 2):
		number += 1
	return number

def stingyCase(total_lambs):
	remaining = total_lambs
	last = 0
	current = 1
	number = 0
	while (remaining >= current):
		remaining -= current
		number += 1
		last, current = current, last + current
	return number

def answer(total_lambs):
	stingy = stingyCase(total_lambs)
	generous = generousCase(total_lambs)

	result = stingy - generous
	print(result)
	return result


answer(2)
#0

answer(10)
#1

answer(13)
#1

answer(143)
#3
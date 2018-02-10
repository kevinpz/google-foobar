#!/usr/bin/env python2

#gauss algorithm taken from here: https://rosettacode.org/wiki/Gaussian_elimination#Python
#as we can't use the numpy python lib

from fractions import Fraction
import copy


def nice_print(tab):
	for row in tab:
		print row
	print

#find the least common multiple in a given list
def find_lcm(mylist):
	max_val = max(mylist)
	cpt, common = 0, 0
	rest = sum(mylist)
	#until we find a common multiple
	while (rest != 0):
		cpt += 1
		#we increase the current number
		common = cpt * max_val
		rest = sum([common % v if v > 0 else 0 for v in mylist])

	return common

#from the original matrix, we create a proba matrix
def create_proba_m(m, size, transition_state_nb):
	sum_by_row = [sum(m[i]) for i in range(size)]

	proba_m = []
	for i in range(size):
		if i < transition_state_nb:
			proba_m.append([Fraction(m[i][x]) / sum_by_row[i] for x in range(size)])
		else:
			proba_m.append([Fraction(1) if i == x else Fraction(0) for x in range(size)])
	return proba_m

#once we have the result; we can find the LCM and put a common denominator for all final states probas
def normalize_res(b, terminal_state_nb):
	den_list = [b[i].denominator for i in range(terminal_state_nb)]
	lcm = find_lcm(den_list)
	res = [b[i].numerator * lcm / den_list[i] for i in range(terminal_state_nb)]
	res.append(lcm)
	return res

#function to inverse the matrix (A = matrix to inverse, B = identity matrix, A * A-1 = I)
def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b

#we use the markov algorithm with absorbing states
def compute_proba(normalize_m, size, terminal_state_nb, transition_state_nb):
	#we cut our matrix in 4 different parts
	q = [[normalize_m[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]
	r = [[normalize_m[i][j] for j in range(transition_state_nb, size)] for i in range(transition_state_nb)]
	idy = [[1 if i == j else 0 for j in range(transition_state_nb)] for i in range (transition_state_nb)]
	iq = [[idy[i][j] - q[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]

	print('q')
	nice_print(q)

	print('r')
	nice_print(r)

	n = gauss(iq, idy)
	#the proba states are given by B = NR
	b = [sum([n[0][y] * r[y][x] for y in range(transition_state_nb)]) for x in range(terminal_state_nb)]

	#once we have the proba states, we need to put the same denominator for all probas
	res = normalize_res(b, terminal_state_nb)

	return res

#reorder matrix, put empty row at the bottom, and reorder the colomn as well
def reorder_m(m, size, transition_state_nb):
	nice_print(m)
	ordered_m = []
	permutation_list = []
	#for each line
	for i in range(size):
		#if we found an empty line
		if(sum(m[i]) != 0):
			permutation_list.append([i, len(ordered_m)])
			ordered_m.append(m[i])

	#add missing final state = empty rows
	for i in range(transition_state_nb):
		ordered_m.append([0 for i in range(size)])


	for orig, dest in permutation_list:
		if orig != dest:
			for k in range(size):
				m[k][orig], m[k][dest] = m[k][dest], m[k][orig]

	nice_print(ordered_m)
	return ordered_m



def answer(m):
	size = len(m)
	terminal_state_nb = sum([1 if sum(m[i]) == 0 else 0 for i in range(size)])
	transition_state_nb = size - terminal_state_nb

	if(transition_state_nb > 0):
		order_m = reorder_m(m, size, transition_state_nb)
		normalize_m = create_proba_m(order_m, size, transition_state_nb)
		#nice_print(normalize_m)
		res = compute_proba(normalize_m, size, terminal_state_nb, transition_state_nb)
	else:
		res=[1,1]
	print(res)

	return res

m=[
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [7, 6, 8, 21]')
 
m=[
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [0, 3, 2, 9, 14]')
 
m=[
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [1, 2, 3]')

m=[
        [0]
  ]
#answer(m)  
#print('--> [1, 1]')
 
m=[
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [1, 2, 3, 4, 5, 15]')
 
m=[
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [4, 5, 5, 4, 2, 20]')
 
m=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [1, 1, 1, 1, 1, 5]')
 
m=[
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

answer(m)  
print('--> [2, 1, 1, 1, 1, 6]')
 
m=[
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [6, 44, 4, 11, 22, 13, 100]')
 
m=[
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
#answer(m)  
#print('--> [1, 1, 1, 2, 5]')

#!/usr/bin/env python2

#find all the multiples of the current nb
def find_multiple_nb(pos, list):
    v = list[pos]
    cpt = len([x for x in list[pos + 1:] if x % v == 0])
    return cpt

#find all the dividers of the current nb
def find_div_nb(pos, list):
    v = list[pos]
    cpt = len([x for x in list[:pos] if v % x == 0])
    return cpt

def answer(l):
    size = len(l)
    #cpt size
    cpt = 0

    #from the second to the end - 1
    for i in xrange(1, size - 1):
        mul_nb = find_multiple_nb(i, l)
        div_nb = find_div_nb(i, l)
        #how many combinations we can make
        cpt += mul_nb * div_nb

    print(cpt)
    return cpt

l = [1, 1, 1]

answer(l)
print('---> 1')

l = [1, 2, 3, 4, 5, 6]

answer(l)
print('---> 3')

l = range(1, 2001)
answer(l)
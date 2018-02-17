#!/usr/bin/env python2
"""
We will calculate our new number with steps with previous number
For instance, for N = 5
size   p
4   +  1
3   +  2
2   +  3
1   +  4

So, we take all the solution from the number p, with the max size < size. 
And if p < size, we add one solution more.

So here, for N = 7
size   p
6   +  1 -> 0 solution + 1 solution because 1 < 6
5   +  2 -> 0 solution + 1 solution because 1 < 6
4   +  3 -> 1 solution from N = 7 with max size at 4 + 1 solution because 3 < 4
3   +  4 -> 0 solution from N = 4 because the only one is with max size = 3
2   +  5 -> 0 solution
"""

def answer(n):
    #init the game with the known values
    #it's array of array. For each N, we keep records of the number of solution
    #And we order it by the max size of the stairs
    sol_list = [[0], [0], [0, 1]]
    
    #until we reach our number
    for v in xrange(4, n + 1):
        cur_value = []
        #fore each decomposition possible
        for p in xrange(1, v):
            #get the max size possible
            size = v - p
            #find all the solution from the previous number with this max stair size
            res = sum(sol_list[p - 1][:size - 1])
            #check if we need to add one stair more
            if p < size:
                res += 1
            #add each solution in an array
            cur_value.append(res)
        #reverse our array to have the lower stair solution in the lower pos
        sol_list.append(list(reversed(cur_value)))

    res = sum(sol_list[n - 1])
    print(res)
    return res

        
n = 3

answer(3)
print('---> 1')

answer(5)
print('---> 2')

answer(6)
print('---> 3')

answer(7)
print('---> 4')

answer(8)
print('---> 5')

answer(9)
print('---> 7')


n = 200
answer(n)
print('---> 487067745')

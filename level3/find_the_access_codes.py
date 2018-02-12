#!/usr/bin/env python2


def answer(l):
    size = len(l)
    triples_list = [[l[i], l[j], l[k]] for i in range(size) for j in range(i, size) for k in range(j, size) if l[j] % l[i] == 0 and l[k] % l[j] == 0 and i < j and j < k]
    print(triples_list)

    res = len(triples_list)
    print(res)
    return res

l = [1, 1, 1]

answer(l)
print('---> 1')

l = [1, 2, 3, 4, 5, 6]

answer(l)
print('---> 3')
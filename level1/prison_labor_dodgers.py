#!/usr/bin/env python2

def answer(x, y):
    #check in which list we have the moved worker
    if len(x) > len(y):
        moved_list = [i for i in x if i not in y]
    else:
        moved_list = [i for i in y if i not in x]
    #as we only have one moved worker, we get it
    value = moved_list[0]
    print(value)
    return value


x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

answer(x,y)
print('---> 6')

x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]

answer(x,y)
print('---> -4')
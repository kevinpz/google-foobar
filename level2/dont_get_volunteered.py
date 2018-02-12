#!/usr/bin/env python2

def nice_print(tab):
    for row in tab:
        print(row)

#recursively update neighbour
def update_path(grid, i, j, cpt):
    #if new size is shorter than the previous one
    if grid[i][j] > cpt:
        grid[i][j] = cpt

        #all posible move with chess knight's moves
        move_list = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
        for a, b in move_list:
            x, y = i + a, j + b
            #if we're still on the chess, update the other cases
            if (x >= 0 and x < 8 and y >= 0 and y < 8):
                update_path(grid, x, y, cpt + 1)


def answer(x, y):
    #init a grid with really huge dist
    grid = [[1000 for i in range(8)] for j in range(8)]
    i = x % 8
    j = x / 8
    #update the path
    update_path(grid, i, j, 0)
    i = y % 8
    j = y / 8
    #get the jump from origin to destination
    res = grid[i][j]
    print(res)
    return res

x = 19
y = 36

answer(x,y)
print('---> 1')

x = 0
y = 1

answer(x,y)
print('---> 3')

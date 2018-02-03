#!/usr/bin/env python2

from copy import deepcopy

def nice_array_print(tab):
	for row in tab:
		print row

def update_pos(maze, tab, height, width, i, j):
	cur_size = tab [i][j]
	possible_move = []
	if i - 1 >= 0:
		possible_move.append([i - 1, j])

	if j - 1 >= 0:
		possible_move.append([i, j - 1])

	if i + 1 < height:
		possible_move.append([i + 1, j])

	if j + 1 < width:
		possible_move.append([i, j + 1])

	for x,y in possible_move:
		maze_val = maze[x][y] * 999 + 1
		if tab[x][y] > cur_size + maze_val:
			tab[x][y] = cur_size + maze_val
			update_pos(maze, tab, height, width, x, y)

def find_path(maze, tab, height, width):
	for i in range(height):
		for j in range(width):
			update_pos(maze, tab, height, width, i, j)


def answer(maze):
	height = len(maze)
	width = len(maze[0])

	tab = [[10000 for i in range(width)] for j in range (height)]
	tab[0][0] = 1

	find_path(maze, tab, height, width)
	size = tab[height - 1][width - 1]

	all_solutions = []
	all_solutions.append(size)

	for i in range(height):
		for j in range(width):
			if maze[i][j] == 1:
				print(i,j)
				backup_tab = deepcopy(tab)
				maze[i][j] = 0
				tab[i][j] -= 999
				update_pos(maze, tab, height, width, i, j)
				size = tab[height - 1][width - 1]
				all_solutions.append(size)
				maze[i][j] = 1
				tab = deepcopy(backup_tab)


	print(min(all_solutions))
	return min(all_solutions)



#maze = [[0, 1, 1], [0, 1, 0], [0, 0, 0]]
#answer(maze)
#7

maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
answer(maze)
#7

#maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
#answer(maze)
#11
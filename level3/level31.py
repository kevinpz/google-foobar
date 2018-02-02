#!/usr/bin/env python2
"""
For the all_paths array, here the code:
0 = never visited
1 = wall
2 = already visited
3 = current path
9 = exit door
"""

from copy import deepcopy

ALLOW_REMOVE = 1

def nice_print(cur_path):
	for row in cur_path:
		print row
	print

def make_move(cur_path, i, j, rem):
	found = 0
	if cur_path[i][j] == 0:
		cur_path[i][j] = 3
	elif cur_path[i][j] == 1 and rem < ALLOW_REMOVE:
		cur_path[i][j] = 3
		rem += 1
	elif cur_path[i][j] == 9:
		cur_path[i][j] = 3
		found = sum(mypath.count(3) for mypath in cur_path)
	else:
		found = -1
	
	print(sum(mypath.count(3) for mypath in cur_path))
	my_path = [cur_path, i, j, rem]
	nice_print(cur_path)
	return found, my_path

def answer(maze):
	height = len(maze)
	width = len(maze[0])
	all_paths = []
	shortest_path = height + width - 1
	sol_path_size = []

	path = deepcopy(maze)
	path[0][0], path[height - 1][width - 1] = 3, 9
	my_path = [path, 0, 0, 0]

	all_paths.append(my_path)

	while all_paths:
		cur_path, i, j, rem = all_paths.pop()

		possible_move = []
		if i + 1 < width:
			possible_move.append([i + 1, j])
		#if i - 1 >= 0:
		#	possible_move.append([i - 1, j])
		if j + 1 < height:
			possible_move.append([i, j + 1])
		#if j - 1 >= 0:
		#	possible_move.append([i, j - 1])

		prev_path = deepcopy(cur_path)
		for i, j in possible_move:
			cur_path = deepcopy(prev_path)
			found, my_path = make_move(cur_path, i, j, rem)
			if found == 0:
				all_paths.append(my_path)
			elif found == shortest_path:
				print("Shortest solution found: " + str(found))
				return found
			elif found > 0:
				sol_path_size.append(found)

	solution = min(sol_path_size)
	print("Short solution found: " + str(solution))
	return solution


maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
answer(maze)
#7

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
answer(maze)
#11

maze = [[0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
answer(maze)
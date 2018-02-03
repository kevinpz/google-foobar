#!/usr/bin/env python2

from copy import deepcopy

def update_pos(maze, tab, height, width, i, j):
	#get our current distance to the start position
	cur_size = tab [i][j]

	#we need to calculate all the posible move (depending on our current position)
	possible_move = []
	if i - 1 >= 0:
		possible_move.append([i - 1, j])
	if j - 1 >= 0:
		possible_move.append([i, j - 1])
	if i + 1 < height:
		possible_move.append([i + 1, j])
	if j + 1 < width:
		possible_move.append([i, j + 1])

	#for each possible move
	for x,y in possible_move:
		#we check if it a empty case, or if there is a wall
		#if no wall, we add 1, if it's a wall, we add a huge value 1000
		move_val = maze[x][y] * 999 + 1
		#now we get the possible new value if we use this path
		new_size = cur_size + move_val
		#and if the new value is lower than the current one, we take it
		if tab[x][y] >new_size:
			tab[x][y] = new_size
			#and we recurse on the new case to propagate it to the other cases
			update_pos(maze, tab, height, width, x, y)

def find_path(maze, tab, height, width):
	#for each case in our maze, we are going to update their distance to the start position
	for i in range(height):
		for j in range(width):
			update_pos(maze, tab, height, width, i, j)

def remove_wall(maze, tab, height, width, all_solutions):
	#now we will try to remove wall
	#so we need to remove all the walls one by one and check for the size
	#and we keep a backup of our original path
	backup_tab = deepcopy(tab)
	for i in range(height):
		for j in range(width):
			#if it's a wall
			if maze[i][j] == 1:
				#remove it
				maze[i][j] = 0
				#decrease the path cost on the current case
				tab[i][j] -= 999
				#and propagate to the other cases
				update_pos(maze, tab, height, width, i, j)
				#and add the new solution to the solution list
				size = tab[height - 1][width - 1]
				all_solutions.append(size)
				#and we put the wall back
				maze[i][j] = 1
				tab = deepcopy(backup_tab)

def answer(maze):
	height = len(maze)
	width = len(maze[0])

	#create a distance array with really huge value : 10000 means the tab is empty
	tab = [[10000 for i in range(width)] for j in range (height)]
	#now we place the startup position with 1
	tab[0][0] = 1

	#let's try without removing wall
	find_path(maze, tab, height, width)
	#get the minimal number of move if we dont remvove any wall
	size = tab[height - 1][width - 1]

	all_solutions = []
	#add the path size if we don't remove any wall
	all_solutions.append(size)

	remove_wall(maze, tab, height, width, all_solutions)

	the_solution = min(all_solutions)
	print(the_solution)
	return the_solution

maze = [[0, 1, 1], [0, 1, 0], [0, 0, 0]]
answer(maze)
#5

maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
answer(maze)
#7

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
answer(maze)
#11
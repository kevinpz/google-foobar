#!/usr/bin/env python2.7

# Using the Ford-Fulkerson algorithm to find the maximum flow in our network

def nice_print(tab):
  for row in tab:
    print(row)

#transform a multi source and multi sink to a single source/sink graph
def transform_path(entrances, exits, path):
    size = len(path)
    entry_nb = len(entrances)
    exits_nb = len(exits)
    new_size = size + 2
    max_bunnies = sum(path[i][j] for i in xrange(size) if i in entrances for j in xrange(size))
    source_row = [max_bunnies if i in entrances else 0 for i in xrange(size)]
    path.insert(0, source_row)

    for row in path:
        row.insert(0, 0)
        row.append(0)

    for row_nb in range(new_size - 1):
        if row_nb - 1 in exits:
            path[row_nb][new_size - 1] = max_bunnies

    sink_row = [0 for i in xrange(new_size)]
    path.append(sink_row)

    return max_bunnies

def bfs(start, end, path, flows, max_bunnies):
    global inf
    length = len(path)
    parents = [-1] * length     
    parents[start] = -2         

    queue = []
    queue.append(start)
    while queue and parents[end] == -1:
        u = queue.pop(0)
        for v in range(length):
            cf = path[u][v] - flows[u][v]
            if cf > 0 and parents[v] == -1:
                queue.append(v)
                parents[v] = u

    if parents[end] == -1:      # if t can not been reached
        return 0, parents

    v = end
    delta = max_bunnies
    while v != start:
        u = parents[v]
        cf = path[u][v] - flows[u][v]
        delta = min(delta, cf)
        v = u

    return delta, parents


def answer(entrances, exits, path):
    max_bunnies = transform_path(entrances, exits, path)
    max_flow = 0
    size = len(path)
    flows = [[0 for i in range(size)] for j in range(size)]
    start = 0
    end = size - 1
    while True:
        ap_flow, parents = bfs(start, end, path, flows, max_bunnies)
        if ap_flow == 0:
            break
        max_flow += ap_flow
        v = end
        while v != start:
            u = parents[v]
            flows[u][v] += ap_flow
            flows[v][u] -= ap_flow
            v = u
    return max_flow

entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
answer(entrances, exits, path)
print('---> 6')

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

answer(entrances, exits, path)
print('---> 16')


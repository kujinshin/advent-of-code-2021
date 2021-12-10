import sys
from collections import deque

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]


def get_adjacents(row, col, row_max, col_max):
    adjacents = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        pos = [row + dx, col + dy]
        if pos[0] >= row_max or pos[0] < 0 or pos[1] >= col_max or pos[1] < 0:
            continue
        adjacents.append(tuple(pos))
    return adjacents


grid = []
for x in data:
    grid.append(list([int(y) for y in x]))

skip = set()

mins = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if not (row, col) in skip:
            val = grid[row][col]
            adjacents = get_adjacents(row, col, len(grid), len(grid[0]))
            counter = len(adjacents)

            for adj in adjacents:
                if grid[adj[0]][adj[1]] > val:
                    counter -= 1
                    skip.add(adj)
                else:
                    skip.add(val)
                    break
            if counter == 0:
                mins.append((row, col, val))


def get_basin_size(row, col, grid, visited):
    q = deque()

    q.append((row, col))
    visited.add((row, col))

    while (len(q) > 0):
        curr_r, curr_c = q.popleft()

        for adj_r, adj_c in get_adjacents(curr_r, curr_c, len(grid),
                                          len(grid[0])):
            if grid[curr_r][curr_c] < grid[adj_r][adj_c] and not (
                    adj_r, adj_c) in visited and grid[adj_r][adj_c] != 9:
                q.append((adj_r, adj_c))
                visited.add((adj_r, adj_c))
    return len(visited)


basins = []

for row, col, _ in mins:
    basins.append(get_basin_size(row, col, grid, set()))

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])

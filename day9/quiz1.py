import sys

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
    grid.append(list(x))

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

risk_level_sum = 0
for _, _, val in mins:
    risk_level_sum += int(val)
    risk_level_sum += 1

print(risk_level_sum)

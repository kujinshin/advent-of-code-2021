import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

def get_adjacents(i, j):
    directions = [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    adjacents = []
    for di, dj in directions:
        adj_i = i + di
        adj_j = j + dj

        if adj_i in range(0, 10) and adj_j in range(0, 10):
            adjacents.append((adj_i, adj_j))

    return adjacents

def all_lighted(s):
    for i in range(10):
        for j in range(10):
            if s[i][j] > 0:
                return False
    return True

s = [[int(y) for y in x] for x in data]

steps = 0
while not all_lighted(s):
    steps += 1
    lighted = set()
    light_others = []

    for i in range(10):
        for j in range(10):
            s[i][j] += 1
            if s[i][j] > 9:
                lighted.add((i,j))
                light_others.append((i, j))

    while len(light_others) > 0:
        light_others_copy = light_others.copy()
        light_others = []

        for i, j in light_others_copy:
            adjs = get_adjacents(i, j)
            for adj_i, adj_j in adjs:
                if (adj_i, adj_j) in lighted:
                    continue
                s[adj_i][adj_j] += 1
                if s[adj_i][adj_j] > 9:
                    lighted.add((adj_i, adj_j))
                    light_others.append((adj_i, adj_j))
    for i in range(10):
        for j in range(10):
            if s[i][j] > 9:
                s[i][j] = 0

print(steps)

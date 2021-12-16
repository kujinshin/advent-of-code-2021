"""
Solution from: https://github.com/DecemberDream/advent-of-code/blob/main/2021/day15/day_15_part_2.py
- It was too slow to run part 2
"""
import sys
from queue import PriorityQueue


def get_neighbours(i, j, grid):
    ret = []
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i = i + di
        new_j = j + dj
        if new_i in range(len(grid)) and new_j in range(len(grid[0])):
            ret.append((new_i, new_j))
    return ret


def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    frontier = PriorityQueue()

    frontier.put((0, start))
    visited = {start}

    while frontier:
        curr_risk, (i, j) = frontier.get()
        neighbours = get_neighbours(i, j, grid)

        if i == goal[0] and j == goal[1]:
            return curr_risk

        for row, col in neighbours:
            if 0 <= row < rows and 0 <= col < cols and (row,
                                                        col) not in visited:
                risk = grid[row][col]
                frontier.put((curr_risk + risk, (row, col)))
                visited.add((row, col))


if __name__ == "__main__":
    input_file = sys.argv[1]

    data = []
    with open(input_file, "r") as f:
        data = [x.rstrip() for x in f.readlines()]

    grid = [[int(y) for y in x] for x in data]
    print(dijkstra(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1)))

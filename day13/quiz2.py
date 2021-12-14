import sys
from pprint import pprint

input_file = sys.argv[1]


def draw_points(points):
    max_x = 0
    max_y = 0
    for point in points:
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])

    drawing = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for point in set(points):
        x = point[0]
        y = point[1]

        drawing[y][x] = "#"

    pprint(["".join(x) for x in drawing])


def fold(points, axis, at_num):
    new_points = []
    if axis == "x":
        for point in points:
            x = point[0]
            y = point[1]

            if x > at_num:
                x = x - 2 * (x - at_num)
            new_points.append((x, y))

    if axis == "y":
        for point in points:
            x = point[0]
            y = point[1]

            if y > at_num:
                y = y - 2 * (y - at_num)
            new_points.append((x, y))
    return new_points


data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

points = []
instructions = []

scanned_all_points = False
for row in data:
    if scanned_all_points:
        instructions.append(row)
    elif row == "":
        scanned_all_points = True
    else:
        points.append([int(x) for x in row.split(",")])

for instruction in instructions:
    instruction = instruction.split(" ")[2]
    axis, at_num = instruction.split("=")
    points = fold(points, axis, int(at_num))

draw_points(points)

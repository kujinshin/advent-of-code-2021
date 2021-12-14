import sys

input_file = sys.argv[1]


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

for instruction in instructions[0:1]:
    instruction = instruction.split(" ")[2]
    axis, at_num = instruction.split("=")
    points = fold(points, axis, int(at_num))

print(len(set(points)))

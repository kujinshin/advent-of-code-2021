import re
import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]


def transform_data(data):
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', data)]
    points = []

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x, y))

    return points


point_map = {}
for points in [transform_data(x) for x in data]:
    for point in points:
        point_map[point] = point_map.get(point, 0) + 1

overlap = 0
for count in point_map.values():
    if count >= 2:
        overlap += 1

print(overlap)

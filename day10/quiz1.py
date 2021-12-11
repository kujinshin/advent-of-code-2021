import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

open_chars = set(["(", "[", "{", "<"])
closed_chars = set([")", "]", "}", ">"])

closed_open_map = {")": "(", "]": "[", "}": "{", ">": "<"}


# Corrupted = An opening bracket has a clear mismatch.
# There may be spare opening brackets
def is_corrupted(s):
    stack = []
    for c in s:
        if c in open_chars:
            stack.append(c)
        elif c in closed_chars:
            latest_bracket = stack.pop(-1)
            if latest_bracket != closed_open_map[c]:
                return True, c
    return False, ""


point_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

point = 0
for line in data:
    corrupted, bracket = is_corrupted(line)
    if corrupted:
        point += point_map.get(bracket)

print(point)

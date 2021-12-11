import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

open_chars = set(["(", "[", "{", "<"])
closed_chars = set([")", "]", "}", ">"])

closed_open_map = {")": "(", "]": "[", "}": "{", ">": "<"}

open_closed_map = {"(": ")", "[": "]", "{": "}", "<": ">"}


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


# Incomplete = All closing brackets have a matching opening bracket,
# but there are spare opening brackets
def is_incomplete(s):
    stack = []
    for c in s:
        if c in open_chars:
            stack.append(c)
        elif c in closed_chars:
            stack.pop(-1)
    if stack == 0:
        return False, []
    stack.reverse()
    return True, "".join([open_closed_map[x] for x in stack])


point_map = {")": 1, "]": 2, "}": 3, ">": 4}

points = []
for line in data:
    corrupted, _ = is_corrupted(line)
    if not corrupted:
        incomplete, missing_brackets = is_incomplete(line)
        if incomplete:
            point = 0
            for c in missing_brackets:
                point = point * 5
                point += point_map[c]
            points.append(point)

print(sorted(points)[len(points) // 2])

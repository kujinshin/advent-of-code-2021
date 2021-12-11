import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

horizontal_position = 0
depth = 0

for row in data:
    command, value = row.split(" ")
    value = int(value)

    if command == "forward":
        horizontal_position += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

print(horizontal_position * depth)

import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

data = [x.split("|")[1].strip().split(" ") for x in data]

count = 0

for x in data:
    for s in x:
        if len(s) == 2 or len(s) == 4 or len(s) == 3 or len(s) == 7:
            count += 1

print(count)

import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

increments = 0
data = [int(x) for x in data]

for i in range(1, len(data)):
    increments += int(data[i] > data[i-1])

print(increments)

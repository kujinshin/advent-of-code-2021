import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

increments = 0
data = [int(x) for x in data]

window_sums = []
for i in range(2, len(data)):
    window_sum = data[i] + data[i - 1] + data[i - 2]
    window_sums.append(window_sum)

for i in range(1, len(window_sums)):
    increments += int(window_sums[i] > window_sums[i - 1])

print(increments)

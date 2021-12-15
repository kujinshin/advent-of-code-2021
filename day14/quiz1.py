import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

template = data[0]

rules = {}
for mapping in data[2:]:
    pair, insert = mapping.split(" -> ")
    rules[pair] = insert

steps = 10

for _ in range(steps):
    new_template = template

    index = 1
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        new_template = new_template[:index] + rules[pair] + new_template[index:]
        index += 2

    template = new_template

counter = {}
for c in template:
    counter[c] = counter.get(c, 0) + 1

print(max(counter.values()) - min(counter.values()))

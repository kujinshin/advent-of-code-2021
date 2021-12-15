import sys
from math import ceil

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

template = data[0]

rules = {}
for mapping in data[2:]:
    pair, insert = mapping.split(" -> ")
    rules[(pair[0], pair[1])] = insert


def get_new_pairs(pairs, rule):
    return [(pairs[0], rule), (rule, pairs[1])]


pairs = {}

for i in range(len(template) - 1):
    pair = (template[i], template[i + 1])
    pairs[pair] = pairs.get(pair, 0) + 1

for _ in range(40):
    new_pairs = {}
    for old_pair, count in pairs.copy().items():
        for new_pair in get_new_pairs(old_pair, rules[old_pair]):
            new_pairs[new_pair] = new_pairs.get(new_pair, 0) + count
    pairs = new_pairs.copy()

counter = {}
for pair, count in pairs.items():
    counter[pair[0]] = counter.get(pair[0], 0) + count
    counter[pair[1]] = counter.get(pair[1], 0) + count

print(ceil(max(counter.values()) / 2) - ceil(min(counter.values()) / 2))

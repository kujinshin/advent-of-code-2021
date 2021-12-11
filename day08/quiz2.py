import sys


def decode_segments(input_data, output_data):
    decode_map = {}

    for x in input_data:
        if len(x) == 2:
            decode_map[1] = x
        elif len(x) == 4:
            decode_map[4] = x
        elif len(x) == 3:
            decode_map[7] = x
        elif len(x) == 7:
            decode_map[8] = x

    for x in input_data:
        if len(x) == 5 and decode_map[1][0] in x and decode_map[1][1] in x:
            decode_map[3] = x
            break

    e_char = set(decode_map[8]) - set(decode_map[3]) - set(decode_map[4])
    e_char = e_char.pop()

    for x in input_data:
        if len(x) == 6 and not e_char in x:
            decode_map[9] = x
            break

    counter = {}
    for x in input_data:
        for c in x:
            counter[c] = counter.get(c, 0) + 1

    f_char = ""
    for k, v in counter.items():
        if v == 9:
            f_char = k
            break

    for x in input_data:
        if f_char not in x:
            decode_map[2] = x
            break

    for x in input_data:
        if len(x) == 5 and not x in decode_map.values():
            decode_map[5] = x
            break

    for x in input_data:
        if len(x) == 6 and set(decode_map[5]) | set([e_char]) == set(x):
            decode_map[6] = x

    for x in input_data:
        if not x in decode_map.values():
            decode_map[0] = x
            break

    sort_str = lambda x: "".join(sorted(x))

    decode_map = dict((sort_str(v), str(k)) for k, v in decode_map.items())

    return (decode_map[sort_str(output_data[0])] +
            decode_map[sort_str(output_data[1])] +
            decode_map[sort_str(output_data[2])] +
            decode_map[sort_str(output_data[3])])


input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

input_data = [x.split("|")[0].strip().split(" ") for x in data]
output_data = [x.split("|")[1].strip().split(" ") for x in data]

total = 0
for i, o in zip(input_data, output_data):
    total += int(decode_segments(i, o))

print(total)

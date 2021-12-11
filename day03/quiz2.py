import sys

input_file = sys.argv[1]

input_data = []
with open(input_file, "r") as f:
    input_data = [x.rstrip() for x in f.readlines()]

bit_count = len(input_data[0])

data = input_data.copy()
for bit_index in range(bit_count):
    common_bit = 0
    ones = []
    zeros = []

    for number in data:
        common_bit += int(number[bit_index])
        if number[bit_index] == "1":
            ones.append(number)
        else:
            zeros.append(number)

    if common_bit >= len(data) / 2:
        data = ones
    else:
        data = zeros

    if len(data) == 1:
        break

oxygen_rating = int(data[0], 2)

data = input_data.copy()
for bit_index in range(bit_count):
    common_bit = 0
    ones = []
    zeros = []

    for number in data:
        common_bit += int(number[bit_index])
        if number[bit_index] == "1":
            ones.append(number)
        else:
            zeros.append(number)

    if common_bit < len(data) / 2:
        data = ones
    else:
        data = zeros

    if len(data) == 1:
        break

co2_rating = int(data[0], 2)

print(oxygen_rating, co2_rating)
print(oxygen_rating * co2_rating)

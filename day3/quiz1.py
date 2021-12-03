import sys

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]

data_count = len(data)
bit_count = len(data[0])
bits = [0 for _ in range(bit_count)]
for number in data:
    for i in range(bit_count):
        if number[i] == "1":
            bits[i] += 1

gamma_rate = [str(int(int(x) > data_count//2)) for x in bits]
gamma_rate = int("".join(gamma_rate), 2)

mask = int("".join(["1" for _ in range(bit_count)]), 2)

epsilon_rate = gamma_rate ^ mask

print(gamma_rate, epsilon_rate)
print(gamma_rate * epsilon_rate)

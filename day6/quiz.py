input_s = input("Initial state: ")
day = int(input("Day: "))

states = [0] * 9

for x in input_s.split(","):
    states[int(x)] += 1

for _ in range(day):
    state0 = states[0]

    for i in range(1, 9):
        states[i-1] = states[i]

    states[8] = state0
    states[6] += state0

print(sum(states))

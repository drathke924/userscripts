with open("day25.txt", "r") as f:
    DATA = list(map(lambda x: x.split("-"), f.read().splitlines()))

states = {}
for l in DATA:
    states[l[0]] = (tuple(l[1]), tuple(l[2]))

steps = 12481997
#steps = 6
state = "a"
position = 0
memory = {}
for i in range(steps):
    if position not in memory.keys():
        memory[position] = 0
    if memory[position]:
        instruct = states[state][1]
    else:
        instruct = states[state][0]
    memory[position] = instruct[0] == "1"
    if instruct[1] == "r":
        position += 1
    elif instruct[1] == "l":
        position -= 1
    state = instruct[2]

print(sum(memory.values()))

with open("day25test.txt", "r") as f:
    DATA = list(map(lambda x: x.split("-"), f.read().splitlines()))

states = {}
for l in DATA:
    states[l[0]] = (tuple(l[1]), tuple(l[2]))

print(states)
#steps = 12481997
steps = 6

state = "a"

position = 0

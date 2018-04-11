with open("day22.txt", "r") as f:
    DATA = f.read().splitlines()

current = (12,12)
infected = set()
dir = "u"
count = 0

def turn(face, inf):
    if inf:
        if face == "u":
            return "r"
        elif face == "r":
            return "d"
        elif face == "d":
            return "l"
        else:
            return "u"
    else:
        if face == "d":
            return "r"
        elif face == "l":
            return "d"
        elif face == "u":
            return "l"
        else:
            return "u"

def move(face, node):
    if face == "u":
        return (node[0], node[1] - 1)
    elif face == "l":
        return (node[0] - 1, node[1])
    elif face == "d":
        return (node[0], node[1] + 1)
    else:
        return (node[0] + 1, node[1])

for i in range(len(DATA)):
    for j in range(len(DATA[i])):
        if DATA[i][j] == "#":
            infected.add((j, i))


for i in range(10000):
    if current in infected:
        infected.remove(current)
        dir = turn(dir, 1)
    else:
        infected.add(current)
        dir = turn(dir, 0)
        count += 1
    current = move(dir, current)


print(count)

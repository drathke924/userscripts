with open("day22.txt", "r") as f:
    DATA = f.read().splitlines()

current = (int(len(DATA) / 2), int(len(DATA) / 2))
infected = set()
weakened = set()
flagged = set()
clean = set()
dir = "u"
count = 0

def turn(face, inf):
    if inf == 1:
        if face == "u":
            return "r"
        elif face == "r":
            return "d"
        elif face == "d":
            return "l"
        else:
            return "u"
    elif inf == 2:
        if face == "u":
            return "d"
        elif face == "r":
            return "l"
        elif face == "d":
            return "u"
        else:
            return "r"
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
        else:
            clean.add((j, i))


for i in range(10000000):
    #if i % 100000 == 0:
    #    print(i)
    #print(str(current) + " " + str(dir))
    if current in infected:
        #print(str(current) + " flagging")
        infected.remove(current)
        flagged.add(current)
        dir = turn(dir, 1)
    elif current in flagged:
        #print(str(current) + " cleaning")
        flagged.remove(current)
        clean.add(current)
        dir = turn(dir, 2)
    elif current in clean:
        #print(str(current) + " weakening")
        clean.remove(current)
        weakened.add(current)
        dir = turn(dir, 0)
    elif current in weakened:
        count += 1
        #print(str(current) + " infecting " + str(count))
        weakened.remove(current)
        infected.add(current)
    else:
        #print(str(current) + " weakening")
        weakened.add(current)
        dir = turn(dir, 0)
    current = move(dir, current)


print(count)

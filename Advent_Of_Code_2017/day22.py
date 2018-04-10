with open("day22.txt", "r") as f:
    DATA = f.read().splitlines()

start = (12,12)
infected = set()

for i in range(len(DATA)):
    for j in range(len(DATA[i])):
        if DATA[i][j] == "#":
            infected.add((i, j))

print(infected)

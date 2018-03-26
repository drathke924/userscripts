with open("day19data.txt", "r") as f:
    DATA = f.read().splitlines()

x = DATA[0].index("|")
y = 0

dir = "down"
partone = []
end = False
current = "|"
step = 0

while not end:
    step += 1
    if dir == "down":
        y += 1
    elif dir == "left":
        x -= 1
    elif dir == "up":
        y -= 1
    elif dir == "right":
        x += 1
    current = DATA[y][x]
    if current.isalpha():
        partone.append(current)
    elif current == "+":
        if dir in ["up", "down"]:
            try:
                if DATA[y][x + 1] != " ":
                    dir = "right"
                else:
                    dir = "left"
            except IndexError:
                dir = "left"
        elif dir in ["right", "left"]:
            try:
                if DATA[y + 1][x] != " ":
                    dir = "down"
                else:
                    dir = "up"
            except IndexError:
                dir = "up"
    elif current == " ":
        end = True

print("".join(partone))
print(step)

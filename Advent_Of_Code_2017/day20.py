with open("day20data.txt", "r") as f:
    DATA = f.read().splitlines()
accel = 0
for i in range(len(DATA)):
    temp = DATA[i].split(" ")[2]
    temp = temp.split(",")
    print(temp)

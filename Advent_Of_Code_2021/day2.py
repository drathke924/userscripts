xone = 0
yone = 0
xtwo = 0
ytwo = 0
aim = 0

def calculate(s):
	global xone
	global yone
	spl = s.split(" ")
	command = spl[0]
	amount = int(spl[1])
	if command == "forward":
		xone += amount
	elif command == "up":
		yone -= amount
	elif command == "down":
		yone += amount

def calctwo(s):
	global xtwo
	global ytwo
	global aim
	spl = s.split(" ")
	command = spl[0]
	amount = int(spl[1])
	if command == "forward":
		xtwo += amount
		ytwo += aim * amount
	elif command == "up":
		aim -= amount
	elif command == "down":
		aim += amount

with open("day2input.txt" , "r") as f:
	data = f.readlines()

for l in data:
	calculate(l)
	calctwo(l)

day2part1 = xone * yone
day2part2 = xtwo * ytwo

print(day2part1)
print(day2part2)

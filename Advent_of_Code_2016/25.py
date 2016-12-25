with open("25.txt", "r") as f:
	data = f.read().splitlines()

def jumpNotZero(reg, instruct, n):
	try:
		instruct[1] = int(instruct[1])
	except:
		instruct[1] = reg[instruct[1]]
	if instruct[1] != 0:
		try:
			instruct[2] = int(instruct[2])
		except:
			instruct[2] = reg[instruct[2]]
		if instruct[2] < 0:
			for i in range(n + instruct[2], n):
				if "jnz" in data[i]:
					jumped = False
					mul = 1
		n += instruct[2]
	else:
		n += 1
	return n

def multiply(reg, instruct):
	reg[instruct[3]] = reg[instruct[1]] * reg[instruct[2]]

def findReg(regi, time):
	reg = regi.copy()
	i = 0
	out = ""
	while i < len(data) and time > 0:
		line = data[i].split()
		if line[0] == "cpy":
			if line[2].isalpha():
				try:
					reg[line[2]] = int(line[1])
				except ValueError:
					reg[line[2]] = reg[line[1]]
		elif line[0] == "jnz":
			i = jumpNotZero(reg, line, i)
			continue
		elif line[0] == "inc":
			reg[line[1]] += 1
		elif line[0] == "dec":
			reg[line[1]] -= 1
		elif line[0] == "mul":
			multiply(reg, line)
		elif line[0] == "out":
			if line[1] in reg.keys():
				 out += str(reg[line[1]])
			else:
				out += line[1]
			time -= 1
		i += 1
	return out

registry = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
test = findReg(registry, 12)
while test != "01" * 6:
	registry["a"] += 1
	test = findReg(registry, 12)

print(registry["a"])

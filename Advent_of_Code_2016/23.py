with open("23.txt", "r") as f:
	readdata = f.read().splitlines()

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
			
def toggle(reg, instruct, n):
	global data
	if reg[instruct[1]] + n < len(data) and reg[instruct[1]] + n >= 0:
		target = data[reg[instruct[1]] + n].split()
		if len(target) == 2:
			if target[0] == "inc":
				target[0] = "dec"
			else:
				target[0] = "inc"
		else:
			if target[0] == "jnz":
				target[0] = "cpy"
			else:
				target[0] = "jnz"
		data[reg[instruct[1]] + n] = " ".join(target)

def multiply(reg, instruct):
	reg[instruct[3]] = reg[instruct[1]] * reg[instruct[2]]

def findReg(reg):
	i = 0
	while i < len(data):
		line = data[i].split()
		if line[0] == "tgl":
			toggle(reg, line, i)
		elif line[0] == "cpy":
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
		i += 1
	return reg["a"]

data = readdata.copy()
registry = {"a" : 7, "b" : 0, "c" : 0, "d" : 0}
print(findReg(registry))

data = readdata.copy()
data[4] = "mul b d a"
for i in range(5, 10):
	data[i] = "nop"
registry = {"a" : 12, "b" : 0, "c" : 0, "d" : 0}
print(findReg(registry))

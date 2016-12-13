from time import time

start_time = time()

reg = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}
i = 0

with open("advent12.txt", "r") as f:
	data = f.read().splitlines()

while i < len(data):
	line = data[i].split()
	if line[0] == "cpy":
		try:
			reg[line[2]] = int(line[1])
		except ValueError:
			reg[line[2]] = reg[line[1]]
	elif line[0] == "jnz":
		if line[1] in reg.keys():
			if reg[line[1]] != 0:
				i += int(line[2])
				continue
		elif int(line[1]) != 0:
			i += int(line[2])
			continue
	elif line[0] == "inc":
		reg[line[1]] += 1
	elif line[0] == "dec":
		reg[line[1]] -= 1
	i += 1

print(reg["a"])

print("Run time: %s" % (time() - start_time))





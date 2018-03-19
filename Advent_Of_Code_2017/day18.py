with open("day18data.txt", "r") as f:
	data = f.read().splitlines()

data = list(map(lambda x: x.split(" "), data))

def partone(datain):
	regset = {}
	step = 0
	lastsound = 0
	while True:
		instruct = list(data[step])
		if instruct[1] not in regset:
			regset[instruct[1]] = 0
		try:
			instruct[2] = int(instruct[2])
		except ValueError:
			instruct[2] = regset[instruct[2]]
		except IndexError:
			pass
		if instruct[0] == "set":
			regset[instruct[1]] = instruct[2]
		elif instruct[0] == "add":
			regset[instruct[1]] += instruct[2]
		elif instruct[0] == "mul":
			regset[instruct[1]] *= instruct[2]
		elif instruct[0] == "mod":
			regset[instruct[1]] = regset[instruct[1]] % instruct[2]
		elif instruct[0] == "snd":
			try:
				instruct[1] = int(instruct[1])
			except ValueError:
				instruct[1] = regset[instruct[1]]
			lastsound = instruct[1]
		elif instruct[0] == "rcv":
			try:
				instruct[1] = int(instruct[1])
			except ValueError:
				instruct[1] = regset[instruct[1]]
			if instruct[1] > 0:
				return lastsound
		elif instruct[0] == "jgz":
			try:
				instruct[1] = int(instruct[1])
			except ValueError:
				instruct[1] = regset[instruct[1]]
			if instruct[1] > 0:
				step += instruct[2]
				continue
		step += 1
		
	
print(partone(data))
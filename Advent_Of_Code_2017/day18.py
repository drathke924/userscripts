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
		
def process(regset, step, stackx, stacky):
	count = 0
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
			stacky.append(instruct[1])
			count += 1
		elif instruct[0] == "rcv":
			if stackx != []:
				regset[instruct[1]] = stackx.pop(-1)
			else:
				return (regset, step, stackx, count)
		elif instruct[0] == "jgz":
			try:
				instruct[1] = int(instruct[1])
			except ValueError:
				instruct[1] = regset[instruct[1]]
			if instruct[1] > 0:
				step += instruct[2]
				continue
		step += 1
	
def parttwo(datain):
	regone = {'p': 0}
	regtwo = {'p': 1}
	stackone = []
	stacktwo = []
	stepone = 0
	steptwo = 0
	sendcount = 0
	changed = True
	test = 0
	while changed:
		regone, stepone, stackone, tempcount = process(regone, stepone, stackone, stacktwo)
		regtwo, steptwo, stacktwo, ignore = process(regtwo, steptwo, stacktwo, stackone)
		if tempcount + ignore != test:
			test = tempcount + ignore
			sendcount += tempcount
		else:
			changed = False
	return(sendcount)

print(partone(data))
print(parttwo(data))
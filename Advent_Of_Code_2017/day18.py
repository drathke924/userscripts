with open("day18data.txt", "r") as f:
	DATA = f.read().splitlines()

DATA = list(map(lambda x: x.split(" "), DATA))

def get(instr, reg):
	try:
		return int(instr)
	except ValueError:
		return reg[instr]


def partone():
	global DATA
	regset = {"a": 0, "b": 0, "c": 0, "i": 0, "p": 0}
	step = 0
	lastsound = 0
	while True:
		instruct = list(DATA[step])
		if instruct[0] == "set":
			regset[instruct[1]] = get(instruct[2], regset)
		elif instruct[0] == "add":
			regset[instruct[1]] += get(instruct[2], regset)
		elif instruct[0] == "mul":
			regset[instruct[1]] *= get(instruct[2], regset)
		elif instruct[0] == "mod":
			regset[instruct[1]] = regset[instruct[1]] % get(instruct[2], regset)
		elif instruct[0] == "snd":
			instruct[1] = get(instruct[1], regset)
			lastsound = instruct[1]
		elif instruct[0] == "rcv":
			get(instruct[1], regset)
			if get(instruct[1], regset) > 0:
				return lastsound
		elif instruct[0] == "jgz":
			get(instruct[1], regset)
			if get(instruct[1], regset) > 0:
				step += get(instruct[2], regset)
				continue
		step += 1

def process(step):
	global DATA

	return 0

def parttwo():
	global DATA
	regone = {'p': 0}
	regtwo = {'p': 1}
	stackone = []
	stacktwo = []
	stepone = 0
	steptwo = 0
	sendcount = 0

	return(sendcount)

print(partone())
print(parttwo())

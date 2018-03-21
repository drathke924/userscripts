with open("day18data.txt", "r") as f:
	DATA = f.read().splitlines()

DATA = list(map(lambda x: x.split(" "), DATA))
def get(instr):
	


def partone():
	global DATA
	regset = {"a": 0, "b": 0, "c": 0, "i": 0, "p": 0}
	step = 0
	lastsound = 0
	while True:
		instruct = list(DATA[step])

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

def process():
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

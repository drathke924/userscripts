from functools import reduce
import os

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
	regset = {"a": 0, "b": 0, "i": 0, "p": 0}
	step = 0
	lastsound = 0
	while step < len(DATA):
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
			if instruct[1] == "1":
				print(get(instruct[1], regset))
			if get(instruct[1], regset) > 0:
				step += get(instruct[2], regset)
				continue
		step += 1

def parttwo():
	global DATA
	regset = [{"a": 0, "b": 0, "i": 0, "p": 0, "f": 0}, {"a": 0, "b": 0, "i": 0, "p": 1, "f": 0}]
	stack = [[], []]
	step = [0, 0]
	waiting = [False, False]
	sendcount = 0
	currentproc = 0
	while waiting[0] == False or waiting[1] == False:
		while True:
			#print(step[currentproc])
			instruct = list(DATA[step[currentproc]])
			#print(str(instruct) + " : " + str(currentproc) + " : " + str(step) + " : " + str(step[currentproc]) + " : " + str(stack) + " : " + str(sendcount))
			if instruct[0] == "set":
				regset[currentproc][instruct[1]] = get(instruct[2], regset[currentproc])
			elif instruct[0] == "add":
				regset[currentproc][instruct[1]] += get(instruct[2], regset[currentproc])
			elif instruct[0] == "mul":
				regset[currentproc][instruct[1]] *= get(instruct[2], regset[currentproc])
			elif instruct[0] == "mod":
				regset[currentproc][instruct[1]] = regset[currentproc][instruct[1]] % get(instruct[2], regset[currentproc])
			elif instruct[0] == "snd":
				waiting[1 - currentproc] = False
				stack[1 - currentproc].append(get(instruct[1], regset[currentproc]))
				if currentproc == 1:
					sendcount += 1
			elif instruct[0] == "rcv":
				if stack[currentproc] == []:
					waiting[currentproc] = True
					currentproc = 1 - currentproc
					break
				else:
					regset[currentproc][instruct[1]] = stack[currentproc].pop(0)
			elif instruct[0] == "jgz":
				if get(instruct[1], regset[currentproc]) > 0:
					step[currentproc] += get(instruct[2], regset[currentproc])
					continue
			step[currentproc] += 1
	return(sendcount)

print(partone())
print(parttwo())

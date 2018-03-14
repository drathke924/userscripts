with open("day8data.txt" , "r") as f:
	data = f.read().splitlines()

allRegisters = {}

def comparison(regi, amnt, cmpr):
	if compare == ">":
		if regi > amnt:
			return True
	elif compare == ">=":
		if regi >= amnt:
			return True
	elif compare == "==":
		if regi == amnt:
			return True
	elif compare == "<":
		if regi < amnt:
			return True
	elif compare == "<=":
		if regi <= amnt:
			return True
	elif compare == "!=":
		if regi != amnt:
			return True
	return False

def incdec(inst, amnt):
	if inst == "inc":
		return amnt
	else:
		return -amnt


for l in data:
	register, instruct, amount, ignore, testreg, compare, compamnt = l.split(' ')
	amount = int(amount)
	compamnt = int(compamnt)
	try:
		allRegisters[register]
	except KeyError:
		allRegisters[register] = 0
	#try:
	if comparison(allRegisters[testreg], compamnt, compare):
		allRegisters[register] += incdec(instruct, amount)
	#except KeyError:
	#	allRegisters[testreg] = 0


print(allRegisters.keys())
print(max(allRegisters.values()))

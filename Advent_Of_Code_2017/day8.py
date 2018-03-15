with open("day8data.txt" , "r") as f:
	data = f.read().splitlines()

allRegisters = {}
highest = -99999

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
	try:
		allRegisters[testreg]
	except KeyError:
		allRegisters[testreg] = 0
	if comparison(allRegisters[testreg], compamnt, compare):
		allRegisters[register] += incdec(instruct, amount)
	highest = max([highest, max(allRegisters.values())])


print(max(allRegisters.values()))
print(highest)
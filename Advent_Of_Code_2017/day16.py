from time import clock

with open("day16data.txt", "r") as f:
	data = f.read().split(",")

timestart = clock()

start = []
for i in range(16):
	start.append(chr(i+97))

output = start

def spin(lst, n):
	lst = list(lst)
	for i in range(n):
		lst.insert(0, lst.pop(-1))
	return lst
	
def exchange(lst, x, y):
	lst = list(lst)
	temp = (lst[x], lst[y])
	lst.pop(y)
	lst.insert(y, temp[0])
	lst.pop(x)
	lst.insert(x, temp[1])
	return lst
	
def partner(lst, a, b):
	lst = list(lst)
	lst = exchange(lst, lst.index(a), lst.index(b))
	return lst

def process(lst, instruct):
	lst = list(lst)
	instruct = instruct.split("/")
	instruct.insert(0, instruct[0][0])
	instruct[1] = instruct[1][1:]
	if instruct[0] == "s":
		lst = spin(lst, int(instruct[1]))
	elif instruct[0] == "x":
		lst = exchange(lst, int(instruct[1]), int(instruct[2]))
	elif instruct[0] == "p":
		lst = partner(lst, instruct[1], instruct[2])
	return lst

def dance(lst, ins, n):
	global start
	perms = ["".join(start)]
	for i in range(n):
		for s in ins:
			lst = process(lst, s)
		if "".join(lst) in perms:
			return(perms[n % len(perms)])
		else:
			perms.append("".join(lst))
	return "".join(lst)


	
print(dance(start, data, 1))
print(dance(start, data, 1000000000))
print(clock() - timestart)
	
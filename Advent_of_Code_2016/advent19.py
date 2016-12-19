import math 

data = 3017957

binary = list(bin(data)[2:])
binary.append(binary.pop(0))
print("Part one")
print(int("".join(binary), 2))



#Slow and useless
'''
def josephus(data):
	elves = []
	for i in range(1, data + 1):
		elves.append(i)

	size = len(elves)
	while size > 1:
		half = math.floor(size/2)
		elves.pop(half)
		elves.append(elves.pop(0))
		size = len(elves)
	return elves[0]
'''


largest = 1
current = 1
working = 1
for i in range(1, data + 1):
	current = i
	if working + 2 > current:
		largest = working
		working = 1
	elif working < largest:
		working += 1
	else:
		working += 2

print(working)
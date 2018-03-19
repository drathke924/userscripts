from time import time

timestart = time()

def spinlockone(step, end):
	out = [0]
	position = 0
	for i in range(1, end + 1):
		position = (position + step) % len(out)
		out.insert(position + 1, i)
		position += 1
	return out

def spinlocktwo(step, end):
	out = 0
	position = 0
	for i in range(1, end + 1):
		position = (position + step) % i
		if position == 0:
			out = i
		position += 1
	return out

partone = spinlockone(394, 2017)
parttwo = spinlocktwo(394, 50000000)
print(partone[partone.index(2017) + 1])
print(parttwo)
print(time() - timestart)
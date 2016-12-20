from collections import deque
from time import time

start_time = time()

data = 1364
position = (1, 1)
distance = 0
exit = (31, 39)
queue = deque([[position, distance]])
checked = set([])
lessthan50 = set([])
new = True
found = False

def is_open(x, y):
	return bin(x**2 + 3*x + 2*x*y + y + y**2 + data)[2:].count("1") % 2 == 0

def neighbors(x, y):
	nb = []
	for x2 in range(x-1, x+2):
		for y2 in range(y-1, y+2):
			if (x2 != x or y2 != y) and (x2 == x or y2 == y) and (x2 >= 0 and y2 >= 0):
				nb.append((x2, y2))
	return nb

while not found:
	position, distance = queue.popleft()
	for i in neighbors(position[0], position[1]):
		if i == exit and not found:
			print(distance + 1)
			found = True
		if i not in checked:
			checked.add(i)
			if is_open(i[0], i[1]):
				if distance + 1 <= 50:
					lessthan50.add(i)
				queue.append([i, distance + 1])

print(len(lessthan50))
		
print(time() - start_time)
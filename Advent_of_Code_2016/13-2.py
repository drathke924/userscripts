from collections import deque
from time import time

start_time = time()

data = 1362
position = (1, 1)
distance = 0
queue = deque([[position, distance]])
checked = set([])
lessthan50 = set([])
new = True

def is_open(x, y):
	return bin(x**2 + 3*x + 2*x*y + y + y**2 + data)[2:].count("1") % 2 == 0

def neighbors(x, y):
	nb = []
	for x2 in range(x-1, x+2):
		for y2 in range(y-1, y+2):
			if (x2 != x or y2 != y) and (x2 == x or y2 == y) and (x2 >= 0 and y2 >= 0):
				nb.append((x2, y2))
	return nb

while distance <= 49:
	position, distance = queue.popleft()
	for i in neighbors(position[0], position[1]):
		print(i)
		print(distance)
		if i not in checked:
			checked.add(i)
			if is_open(i[0], i[1]):
				if distance + 1 <= 50:
					lessthan50.add(i)
				queue.append([i, distance + 1])

print(len(lessthan50))
		
print(time() - start_time)
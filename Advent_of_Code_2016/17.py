from time import clock
from collections import deque
import hashlib

start_time = clock()

data = "pxxbnzuo"
frontier = deque()
pos = (0, 0)
vault = (3, 3)
found = False
frontier.append((data, pos))
maxlen = 0

def neighbors(node):
	doors = ["u", "d", "l", "r"]
	m = hashlib.md5()
	m.update(node.encode("utf-8"))
	hsh = m.hexdigest()
	unlocked = []
	for i, c in enumerate(hsh[0:4]):
		if c in "bcdef":
			unlocked.append(doors[i])
	return unlocked

while len(frontier) > 0:
	working, position = frontier.popleft()
	if position == vault:
		if not found:
			print(working[8:])
			print((clock() - start_time) * 1000)
			found = True
		if len(working[8:]) > maxlen:
			maxlen = len(working[8:])
		continue
	for c in neighbors(working):
		if c == "u" and position[1] > 0:
			frontier.append((working + "U", (position[0], position[1] - 1)))
		elif c == "d" and position[1] < 3:
			frontier.append((working + "D", (position[0], position[1] + 1)))
		elif c == "l" and position[0] > 0:
			frontier.append((working + "L", (position[0] - 1, position[1])))
		elif c == "r" and position[0] < 3:
			frontier.append((working + "R", (position[0] + 1, position[1])))

print(maxlen)
print((clock() - start_time) * 1000)

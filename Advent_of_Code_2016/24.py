from collections import deque
from itertools import permutations

with open("24.txt", "r") as f:
	data = f.read().splitlines()

datamap = {}
start_node = ()
width = len(data[0])
height = len(data)
needToFind = set(["0", "1", "2", "3", "4", "5", "6", "7"])
foundPairs = {}
POIs = set()
distances = []

for y in range(len(data)):
	for x in range(len(data[y])):
		datamap[(x, y)] = data[y][x]
		if datamap[(x, y)] == "0":
			start_node = (x, y)
		if datamap[(x, y)] in needToFind:
			POIs.add((datamap[(x, y)], (x, y)))

def neighbors(node):
	global width
	global height
	x, y = node
	nb = []
	for x2 in range(x-1, x+2):
		for y2 in range(y-1, y+2):
			if (x2 != x or y2 != y) and (x2 == x or y2 == y) and (x2 >= 0 and y2 >= 0) and x2 < width and y2 < height:
				nb.append((x2, y2))
	return nb

def findPOI(start, POI):
	global datamap
	global needToFind
	global foundPairs
	found = set([POI])
	visited = set([])
	for i in needToFind:
		if tuple(map(str, sorted([POI, i]))) in foundPairs.keys():
			found.add(i)
	dist = 0
	frontier = deque()
	frontier.append((start, dist))
	while len(found) != len(needToFind):
		current, dist = frontier.popleft()
		if current not in visited:
			visited.add(current)
		for node in neighbors(current):
			sym = datamap[node]
			if node not in visited:
				if sym != "#":
					if sym in needToFind:
						if sym not in found:
							found.add(sym)
							foundPairs[tuple(map(str, sorted([sym, POI])))] = dist + 1
					frontier.append((node, dist + 1))
					visited.add(node)
					

						


	
	
for i in POIs:
	findPOI(i[1], i[0])


for perm in permutations(needToFind):
	if perm[0] == "0":
		distance = 0
		for i, c in enumerate(perm):
			if i < len(perm) - 1:
				distance += foundPairs[tuple(map(str, sorted([c, perm[i + 1]])))]
		distances.append(distance)

print(min(distances))

distances = []
for perm in permutations(needToFind):
	if perm[0] == "0":
		distance = 0
		for i, c in enumerate(perm):
			if i < len(perm) - 1:
				distance += foundPairs[tuple(map(str, sorted([c, perm[i + 1]])))]
			else:
				distance += foundPairs[("0", c)]
		distances.append(distance)

print(min(distances))

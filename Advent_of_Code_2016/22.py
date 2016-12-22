from itertools import permutations as perm
from collections import deque

nodes = {}
start_node = (37, 0)
goal_node = (0, 0)
moved = set()
wall = set()
datanode = start_node
maze = []

with open("22.txt", "r") as f:
	data = f.read().splitlines()

def neighbors(node):
	x, y = node
	nb = []
	for x2 in range(x-1, x+2):
		for y2 in range(y-1, y+2):
			if (x2 != x or y2 != y) and (x2 == x or y2 == y) and (x2 >= 0 and y2 >= 0) and x2 <= 37 and y2 <= 23:
				nb.append((x2, y2))
	return nb

for line in data:
	line = line.split()
	node = line[0].split("-")
	x = int(node[1][1:])
	y = int(node[2][1:])
	nodes[(x, y)] = (int(line[2][:-1]), int(line[3][:-1]))

for i in nodes.keys():
	if nodes[i][0] > 300:
		wall.add(i)

def partOne(nods):
	pairs = set()
	for i in perm(nods.keys(), 2):
		if nods[i[0]][0] > 0 and nods[i[0]][0] < nods[i[1]][1] and (i[0], i[1]) not in pairs:
			pairs.add((i[0], i[1]))
	return pairs

def partTwo(start, goal):
	global nodes
	global wall
	goToStart = True
	frontier = deque()
	visited = set()
	for i in nodes.keys():
		if nodes[i][0] == 0:
			hole = i
			break
	frontier.append((hole, 0, abs(hole[0] - start[0]) + abs(hole[1] - start[1])))
	while len(frontier) > 0 and hole != goal:
		current, steps, dist = frontier.popleft()
		for i in neighbors(current):
			if goToStart:
				idist = abs(i[0] - start[0]) + abs(i[1] - start[1])
			else:
				idist = abs(i[0] - goal[0]) + abs(i[1] - goal[1])
			if i not in wall and idist <= dist + 1 and i not in visited:
				visited.add(i)
				if i == start and goToStart:
					goToStart = False
					frontier.clear()
					visited.clear()
					frontier.append((start, steps + 1, abs(i[0] - goal[0]) + abs(i[1] - goal[1])))
					break
				elif i == goal:
					return steps
				elif not goToStart:
					frontier.append((i, steps + 5, idist))
				else:
					frontier.append((i, steps + 1, idist))





'''
for y in range(23):
	maze.append([])
	for x in range(38):
		if (x, y) in wall:
			maze[y].append("|||")
		elif nodes[(x, y)][0] == 0:
			maze[y].append("_/" + str(nodes[(x, y)][1]))
		else:
			maze[y].append(str(nodes[x, y][0]) + "/" + str(nodes[(x,y)][1]))

for i in maze:
	print(" ".join(i))
'''

print(len(partOne(nodes)))
print(partTwo(start_node, goal_node))


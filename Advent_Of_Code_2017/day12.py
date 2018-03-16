with open("day12data.txt", "r") as f:
	data = f.read().splitlines()

graph = {}

village = []
groups = []

def group(villager, grp):
	global graph
	if villager not in grp:
		grp.append(villager)
	for x in graph[villager]:
		if x not in grp:
			for y in group(x, grp):
				if y not in grp:
					grp.append(y)
	return grp

for i in range(len(data)):
	data[i] = data[i].split(' ')
	data[i].pop(1)

for x in data:
	for i in range(len(x)):
		if i == 0:
			graph[x[i]] = []
		else:
			if x[i][-1] == ",":
				x[i] = x[i][:-1]
			graph[x[0]].append(x[i])


for x in graph.keys():
	if x not in village:
		xgroup = group(x, [])
		village += xgroup
		groups.append(xgroup)

print(len(group("0", [])))
print(len(groups))
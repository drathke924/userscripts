class GridWalker:
	def __init__(self, origin):
		self.pos = list(origin)
	
	def ne(self):
		self.pos[0] -= 1
		self.pos[1] += 1
	
	def nw(self):
		self.pos[2] -= 1
		self.pos[0] += 1
	
	def se(self):
		self.pos[0] -= 1
		self.pos[2] += 1
	
	def sw(self):
		self.pos[1] -= 1
		self.pos[0] += 1
	
	def north(self):
		self.pos[2] -= 1
		self.pos[1] += 1
	
	def south(self):
		self.pos[1] -= 1
		self.pos[2] += 1
	
with open("day11data.txt", "r") as f:
	data = f.read().split(",")
	
child = GridWalker([0,0,0])

farthest = 0

for x in data:
	distance = 0
	if x == "ne":
		child.ne()
	if x == "nw":
		child.nw()
	if x == "se":
		child.se()
	if x == "sw":
		child.sw()
	if x == "s":
		child.south()
	if x == "n":
		child.north()
	for i in child.pos:
		if i > 0:
			distance += i
	if farthest < distance:
		farthest = distance

distance = 0
for i in child.pos:
	if i > 0:
		distance += i

print(distance)
print(farthest)



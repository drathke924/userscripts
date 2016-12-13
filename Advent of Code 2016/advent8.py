display = []
count = 0

def rect(a, b, matrix):
	for i in range(0, a):
		for j in range(0, b):
			if j < 6:
				matrix[j][i] = "#"
	return matrix

def row(a, b, matrix):
	for i in range(b):
		matrix[a].insert(0, matrix[a].pop(-1))
	return matrix

def col(a, b, matrix):
	for i in range(b):
		temp = matrix[-1][a]
		for j in range(0, 5):
			matrix[5-j][a] = matrix[5-(j+1)][a]
		matrix[0][a] = temp
	return matrix

for i in range(0, 6):
	display.append([])
	for j in range(0, 50):
		display[i].append("_")

with open ("advent8.txt", 'r') as f:
	data = f.read().splitlines()
		
for line in data:
	if "=" in line:
		instruct = line[0:line.index("=")].split() + line[line.index("=") + 1:].split()
		if instruct[1] == "column":
			display = col(int(instruct[3]), int(instruct[5]), display)
		elif instruct[1] == "row":
			display = row(int(instruct[3]), int(instruct[5]), display)
	else:
		instruct = line[5:].split('x')
		rect(int(instruct[0]), int(instruct[1]), display)

for i in range(6):
	count += display[i].count("#")
	print("".join(display[i]))
	

print(count)




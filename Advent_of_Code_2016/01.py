direction = [1, 0, 0, 0]
location = [0, 0]
visited = []
solved = False

file = open('advent1.txt', 'r')

instructions = file.read().split()

file.close()

for item in instructions:
	if item[-1] == ',':
		item = item[0:-1]

	steps = int(item[1:])

	if item[0] == 'L':
		direction.append(direction.pop(0))
	else:
		direction.insert(0, direction.pop(3))

	for i in range(steps):
		if direction[0]:
			location[0] += 1
		elif direction[1]:
			location[1] += 1
		elif direction[2]:
			location[0] -= 1
		elif direction[3]:
			location[1] -= 1
		if location not in visited:
			visited.append(list(location))
		elif not solved:
			print(location)
			print(abs(location[0]) + abs(location[1]))
			solved = True

print(location)
print(abs(location[0]) + abs(location[1]))
		


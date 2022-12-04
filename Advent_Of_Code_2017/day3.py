from math import sqrt

def fill_the_grid(input):
	output = {}
	step = 1
	travel = 1
	# right = 0, up = 1, left = 2, down = 3
	direction = 0
	x = 0
	y = 0
	output[step] = (x, y)
	while step < input:
		for i in range(0, 2):
			for j in range(0, travel):
				step += 1
				if direction == 0:
					x += 1
				elif direction == 1:
					y += 1
				elif direction == 2:
					x -= 1
				else:
					y -= 1
				output[step] = (x, y)
			direction = (direction + 1) % 4
		travel += 1
	return output

def build_the_grid(input):
	output = {}
	size = int((int(sqrt(input)) + 1)/2) + 1
	grid = fill_the_grid(input)
	step = 1
	num = 1
	for i in range(size * -1, size + 1):
		for j in range(size * -1, size + 1):
			output[(i, j)] = 0
	#Do the first step
	location = grid[step]
	output[location] = num
	step += 1
	while num < input:
		location = grid[step]
		x, y = location
		num = output[(x + 1, y + 1)] + output[(x + 1, y)] + output[(x + 1, y - 1)] + output[(x, y + 1)] + output[(x, y - 1)] + output[(x - 1, y + 1)] + output[(x - 1, y)] + output[(x - 1, y - 1)]
		output[location] = num
		step += 1
	return num

data = int(input("Input: "))
part_one_part_one = fill_the_grid(data)[data]
part_one = abs(part_one_part_one[0]) + abs(part_one_part_one[1])
print("Part One: " + str(part_one))
print("Part Two: " + str(build_the_grid(data)))

#print(fill_the_grid(50))

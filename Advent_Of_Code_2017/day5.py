with open('day5data.txt', 'r') as f:
	data_one = list(map(int, f.readlines()))

data_two = list(data_one)

part_one = 0
position = 0
last_position = 0
while position < len(data_one):
	last_position = position
	position += data_one[position]
	data_one[last_position] += 1
	part_one += 1

part_two = 0
position = 0
last_position = 0
while position < len(data_two):
	last_position = position
	position += data_two[position]
	if data_two[last_position] >= 3:
		data_two[last_position] -= 1
	else:
		data_two[last_position] += 1
	part_two += 1

print('Part One: ' + str(part_one))
print('Part Two: ' + str(part_two))

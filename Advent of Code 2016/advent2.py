sequence = []

file = open("advent2.txt", 'r')
instructions = file.read().split()
file.close() 

for item in instructions:
	button = [0, 0]
	for char in item:
		if char == 'R':
			if button[0] < 1:
				button[0] += 1
		elif char == 'L':
			if button[0] > -1:
				button[0] -= 1
		elif char == 'U':
			if button[1] < 1:
				button[1] += 1
		elif char == 'D':
			if button[1] > -1:
				button[1] -= 1
	if button == [-1, 1]:
		sequence.append(1)
	elif button == [0, 1]:
		sequence.append(2)
	elif button == [1, 1]:
		sequence.append(3)
	elif button == [-1, 0]:
		sequence.append(4)
	elif button == [0, 0]:
		sequence.append(5)
	elif button == [1, 0]:
		sequence.append(6)
	elif button == [-1, -1]:
		sequence.append(7)
	elif button == [0, -1]:
		sequence.append(8)
	elif button == [1, -1]:
		sequence.append(9)
	
print(sequence)
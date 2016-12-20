seek = 0


with open ("09.txt", "r") as f:
	datum = f.read()

def partOne(data):
	seek = 0
	instruct = []
	while seek < len(data):
		if data[seek] == "(":
			seekend = data[seek:].find(")") + seek
			instruct = list(map(int, data[seek + 1:seekend].split('x')))
			data = data[:seek] + data[seekend+1: seekend+instruct[0]+1] * instruct[1] + data[seekend + instruct[0] + 1:]
			seek = seekend + (instruct[0] * instruct[1]) - len(data[seek:seekend + 1])
		seek += 1
	return len(data)

def partTwo(string):
	total = 0
	seek = 0
	instruct = []
	while seek < len(string):
		if string[seek] == "(":
			seekend = string[seek:].find(")") + seek
			instruct = list(map(int, string[seek + 1:seekend].split('x')))
			total += partTwo(string[seekend+1: seekend+instruct[0]+1]) * instruct[1]
			seek = seekend + instruct[0]
		else:
			with open("advent9out.txt", "a") as f:
				f.write(string[seek])
			total += 1
		seek += 1
	return total

print(partOne(datum))
print(partTwo(datum))
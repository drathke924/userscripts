seek = 0
instruct = []

with open ("advent9.txt", "r") as f:
	data = f.read()

while seek < len(data):
	if data[seek] == "(":
		seekend = data[seek:].find(")") + seek
		instruct = list(map(int, data[seek + 1:seekend].split('x')))
		data = data[:seek] + data[seekend+1: seekend+instruct[0]+1] * instruct[1] + data[seekend + instruct[0] + 1:]
		seek = seekend + (instruct[0] * instruct[1]) - len(data[seek:seekend + 1])
	seek += 1

print(len(data))
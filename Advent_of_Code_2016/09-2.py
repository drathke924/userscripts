total = 0

with open ("advent9.txt", "r") as f:
	data = f.read()

def decomp(string):
	total = 0
	seek = 0
	while seek < len(string):
		if string[seek] == "(":
			seekend = string[seek:].find(")") + seek
			instruct = list(map(int, string[seek + 1:seekend].split('x')))
			total += decomp(string[seekend+1: seekend+instruct[0]+1]) * instruct[1]
			seek = seekend + instruct[0]
		else:
			with open("advent9out.txt", "a") as f:
				f.write(string[seek])
			total += 1
		seek += 1
	return total

print(decomp(data))
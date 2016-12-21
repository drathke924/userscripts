with open("21.txt", "r") as f:
	data = f.read().splitlines()

start = list("abcdefgh")
scram = list("fbgdceah")

def back(lst, n):
	for i in range(n):
		lst.append(lst.pop(0))
	return lst

def forward(lst, n):
	for i in range(n):
		lst.insert(0, lst.pop(len(lst)-1))
	return lst



def scramble(word):
	global data
	newdata = data.copy()
	for line in newdata:
		line = line.split()
		if line[0] == "reverse":
			word = word[0:int(line[2])] + word[int(line[2]):int(line[4])+1][::-1] + word[int(line[4]) + 1:]
		elif line[0] == "rotate":
			if line[1] == "based":
				index = word.index(line[6])
				if index >= 4:
					word = forward(word, 1)
				word = forward(word, index + 1)
			else:
				if line[1] == "left":
					word = back(word, int(line[2]))
				elif line[1] == "right":
					word = forward(word, int(line[2]))
		elif line[0] == "swap":
			if line[1] == "letter":
				temp = word.index(line[5])
				word[word.index(line[2])] = line[5]
				word[temp] = line[2]
			else:
				temp = word[int(line[2])]
				word[int(line[2])] = word[int(line[5])]
				word[int(line[5])] = temp
		elif line[0] == "move":
			temp = word.pop(int(line[2]))
			word.insert(int(line[5]), temp)

	return "".join(word)

def unscramble(word):
	global data
	newdata = data.copy()[::-1]
	for line in newdata:
		line = line.split()
		if line[0] == "reverse":
			word = word[0:int(line[2])] + word[int(line[2]):int(line[4])+1][::-1] + word[int(line[4]) + 1:]
		elif line[0] == "rotate":
			if line[1] == "based":
				index = word.index(line[6])
				if index == 0 or index == 1:
					word = back(word, 1)
				elif index == 2:
					word = forward(word, 2)
				elif index == 3:
					word = back(word, 2)
				elif index == 4:
					word = forward(word, 1)
				elif index == 5:
					word = back(word, 3)
				elif index == 7:
					word = back(word, 4)
			else:
				if line[1] == "left":
					word = forward(word, int(line[2]))
				elif line[1] == "right":
					word = back(word, int(line[2]))
		elif line[0] == "swap":
			if line[1] == "letter":
				temp = word.index(line[5])
				word[word.index(line[2])] = line[5]
				word[temp] = line[2]
			else:
				temp = word[int(line[2])]
				word[int(line[2])] = word[int(line[5])]
				word[int(line[5])] = temp
		elif line[0] == "move":
			temp = word.pop(int(line[5]))
			word.insert(int(line[2]), temp)

	return "".join(word)

print(scramble(start))
print(unscramble(scram))
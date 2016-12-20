chars = [[], [], [], [], [], [], [], []]
answer = ""

with open ("06.txt", 'r') as f:
	data = f.read().splitlines()

for line in data:
	line = line[0:-1]
	for i in range(0, len(line)):
		chars[i].append(line[i])

def partOne(chars):
	answer = ""
	for charset in chars:
		checked = []
		most = ['a', 0]
		for char in charset:
			if char not in checked:
				checked.append(char)
				if charset.count(char) > most[1]:
					most = [char, charset.count(char)]
		answer += most[0]
	return answer

def partTwo(chars):
	answer = ""
	for charset in chars:
		checked = []
		least = ['a', 1000]
		for char in charset:
			if char not in checked:
				checked.append(char)
				if charset.count(char) < least[1]:
					least = [char, charset.count(char)]
		answer += least[0]
	return answer

print(partOne(chars))
print(partTwo(chars))

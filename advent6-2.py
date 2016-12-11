chars = [[], [], [], [], [], [], [], []]
answer = ""

with open ("advent6.txt", 'r') as f:
	data = f.readlines()

for line in data:
	line = line[0:-1]
	for i in range(0, len(line)):
		chars[i].append(line[i])

for charset in chars:
	checked = []
	least = ['a', 1000]
	print(charset)
	for char in charset:
		if char not in checked:
			checked.append(char)
			if charset.count(char) < least[1]:
				least = [char, charset.count(char)]
	answer += least[0]

print(answer)

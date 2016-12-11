chars = [[], [], [], [], [], [], [], []]
answer = ""

with open ("advent6.txt", 'r') as f:
	data = f.readlines()

for line in data:
	line = line[0:-1]
	for i in range(0, len(line)):
		print(i)
		chars[i].append(line[i])

for charset in chars:
	checked = []
	most = ['a', 0]
	for char in charset:
		if char not in checked:
			checked.append(char)
			if charset.count(char) > most[1]:
				most = [char, charset.count(char)]
	answer += most[0]

print(answer)

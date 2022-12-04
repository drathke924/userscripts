with open("input1.txt" , "r") as f:
	data = list(map(int, f.readlines()))

for n in data:
	if 2020-n in data:
		print("Day 1 Part 1: " + str(n*(2020-n)))
		break

found = False
for i in range(0, len(data)):
	for j in range(i + 1, len(data)):
		if 2020 - (data[i]+data[j]) in data:
			print("Day 1 Part 2: " + str(data[i]*data[j]*(2020 - (data[i]+data[j]))))
			print(str(data[i]) + " " + str(data[j]))
			found = True
			break
	if found:
		break

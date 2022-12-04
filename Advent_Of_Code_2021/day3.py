def splitint(l):
	return list(map(int, list(l.strip())))

with open("day3input.txt" , "r") as f:
	data = list(map(splitint, f.readlines()))

print(data)

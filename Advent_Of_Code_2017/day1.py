with open("day1data.txt" , "r") as f:
	data = f.read().strip()

partOne = 0
partTwo = 0

for i in range(0, len(data)):
	j = (i + 1) % len(data)
	k = (i + int(len(data)/2)) % len(data)
	if data[i] == data[j]:
		partOne += int(data[i])
	if data[i] == data[k]:
		partTwo += int(data[i])

print("Part One: " + str(partOne))
print("Part Two: " + str(partTwo))

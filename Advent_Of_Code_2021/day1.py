with open("day1input.txt" , "r") as f:
	data = list(map(int, f.readlines()))

day1part1 = 0
day1part2 = 0

for i in range(1, len(data)):
	if data[i] > data[i-1]:
		day1part1 += 1

prevsum = 1000000
for i in range(2, len(data)):
	currentsum = data[i-2] + data[i-1] + data[i]
	if currentsum > prevsum:
		day1part2 += 1
	prevsum = currentsum

print(day1part1)
print(day1part2)

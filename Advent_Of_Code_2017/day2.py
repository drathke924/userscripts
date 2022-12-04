def split_toint(s):
	return list(map(int, s.split()))

def evenly_divisble(input):
	input.sort(reverse=True)
	for i in range(0, len(input)):
		for j in range(i + 1, len(input)):
			if input[i] % input[j] == 0:
				return int(input[i]/input[j])

def part_one(input):
	output = 0
	for l in input:
		output += max(l) - min(l)
	return output

def part_two(input):
	output = 0
	for l in input:
		output += evenly_divisble(l)
	return output

with open("day2data.txt" , "r") as f:
	data = list(map(split_toint, f.readlines()))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))

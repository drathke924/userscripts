from collections import defaultdict

def diffs(data_in):
    all_diff = {3:0,1:0}
    for adapter, current in zip(data_in[1:], data_in):
        all_diff[adapter - current] += 1
    return all_diff

def part_one(data_in):
    differences = diffs(data_in)
    return differences[1] * differences[3]

def part_two(data_in):
    arrangements = defaultdict(int, {0: 1})
    for adapter in data_in[1:]:
        arrangements[adapter] = arrangements[adapter - 1] + arrangements[adapter - 2] + arrangements[adapter - 3]
    return arrangements[data_in[-1]]

with open("input10.txt" , "r") as f:
	data = sorted(list(map(int, f.read().split("\n"))))

data.insert(0,0)
data.append(data[-1] + 3)


print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
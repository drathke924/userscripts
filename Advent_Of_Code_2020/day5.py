def prep_data(data_in):
    row = int("0b" + data_in[0:7].replace("B", "1").replace("F", "0"), 2)
    column = int("0b" + data_in[7:10].replace("R", "1").replace("L", "0"), 2)
    return row * 8 + column

def part_one(data_in):
    return max(data_in)

def part_two(data_in):
    for i in range(min(data_in), max(data_in)):
        if (i in data_in) != True:
            return i
    return None

with open("input5.txt" , "r") as f:
	data = list(map(prep_data, f.read().split("\n")))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
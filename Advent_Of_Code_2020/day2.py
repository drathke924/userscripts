def prep_line(line):
    split_line = line.split()
    amount = list(map(int, split_line[0].split("-")))
    character = split_line[1][0]
    password = split_line[2].strip()
    return (amount, character, password)

with open("input2.txt" , "r") as f:
	data = list(map(prep_line, f.readlines()))

def part_one(passwords):
    result = 0
    for test in passwords:
        count = test[2].count(test[1])
        if test[0][0] <= count <= test[0][1]:
            result += 1
    return result

def part_two(passwords):
    result = 0
    for test in passwords:
        in_pos_one = test[1] == test[2][test[0][0] - 1]
        in_pos_two = test[1] == test[2][test[0][1] - 1]
        if in_pos_one != in_pos_two:
            result += 1
    return result

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
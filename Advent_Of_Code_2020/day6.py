def prep_data(data_in):
    return data_in.split("\n")

def part_one(data_in):
    result = 0
    for group in data_in:
        answers = set()
        for person in group:
            answers = answers.union(set(person))
        result += len(answers)
    return result

def part_two(data_in):
    result = 0
    for group in data_in:
        answers = set(group[0])
        for person in group:
            answers = answers.intersection(set(person))
        result += len(answers)
    return result

with open("input6.txt" , "r") as f:
	data = list(map(prep_data, f.read().split("\n\n")))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
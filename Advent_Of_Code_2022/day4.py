def prep_data(data_in):
    ranges = data_in.split(",")
    range_one = tuple(map(int, ranges[0].split("-")))
    range_two = tuple(map(int, ranges[1].split("-")))
    set_one = set(range(range_one[0], range_one[1] + 1))
    set_two = set(range(range_two[0], range_two[1] + 1))
    return (set_one, set_two)

def part_one(data_in):
    result = 0
    for line in data_in:
        range_one = line[0]
        range_two = line[1]
        intersect = range_two.intersection(range_one)
        if intersect == range_two or intersect == range_one:
            result += 1
    return result

def part_two(data_in):
    result = 0
    for line in data_in:
        range_one = line[0]
        range_two = line[1]
        if range_one.isdisjoint(range_two) != True:
            result += 1
    return result

with open("day4.txt" , "r") as f:
    data = tuple(map(prep_data, f.readlines()))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))


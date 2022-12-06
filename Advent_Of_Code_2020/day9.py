def part_one(data_in, preamble):
    start, current, found = 0, preamble, False
    while not found:
        check_nums = data_in[start:current]
        curr_num = data_in[current]
        for i in check_nums:
            if curr_num - i != i and (curr_num - i) not in check_nums:
                found = True
            else:
                found = False
                break
        start += 1
        current += 1
    return curr_num

def search_for_sum(data_in, size, target):
    found, result = False, 0
    for i in range(0, len(data_in)):
        check_nums = data_in[i:i+size]
        if max(check_nums) < target and sum(check_nums) == target:
            found = True
            result = max(check_nums) + min(check_nums)
    return result, found

def part_two(data_in, target):
    result, found, search_size = 0, False, 2
    while not found and search_size < len(data_in):
        result, found = search_for_sum(data_in, search_size, target)
        search_size += 1
    return result

with open("input9.txt" , "r") as f:
	data = list(map(int, f.read().split("\n")))

part_one_result = part_one(data, 25)
print("Part One: " + str(part_one_result))
print("Part Two: " + str(part_two(data, part_one_result)))
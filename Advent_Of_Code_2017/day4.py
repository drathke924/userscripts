def split_string(string_in):
	return string_in.split()

def split_sort_join(string_in):
	s = ""
	string_out = []
	return s.join(sorted(list(string_in)))

with open('day4data.txt', 'r') as f:
	data = list(map(split_string, f.readlines()))

part_one = 0
part_two = 0
for l_in in data:
	repeat = list(set(l_in))
	anagram = list(set(map(split_sort_join, l_in)))
	if len(l_in) == len(repeat):
		part_one += 1
	if len(l_in) == len(anagram):
		part_two += 1


print("Part One: " + str(part_one))
print("Part Two: " + str(part_two))

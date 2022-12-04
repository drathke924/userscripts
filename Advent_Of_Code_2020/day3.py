def prep_line(line):
    return tuple(line.strip())

with open("input3.txt" , "r") as f:
	data = tuple(map(prep_line, f.readlines()))

def check_slope(tree_map, step_x, step_y):
    num_trees = 0
    width = len(tree_map[0])
    x = 0
    y = 0
    while y < len(tree_map):
        if tree_map[y][x] == '#':
            num_trees += 1
        x = (x + step_x) % width
        y += step_y
    return num_trees

part_one = check_slope(data, 3, 1)
print("Part One: " + str(part_one))
part_two = check_slope(data, 1, 1) * part_one * check_slope(data, 5, 1) * check_slope(data, 7, 1) * check_slope(data, 1, 2)
print("Part Two: " + str(part_two))
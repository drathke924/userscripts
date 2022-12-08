from math import prod

def generate_map(data_in):
    map_out = {}
    for y in range(0, len(data_in)):
        for x in range(0, len(data_in[y])):
            current_num = data_in[y][x]
            map_out[(x, y)] = current_num
    return map_out, len(data_in[y]), len(data_in)

def is_seen(x, y, full_map, map_size_x, map_size_y):
    height = full_map[(x,y)]
    seen = [1, 1, 1, 1]
    for i in range(0, x):
        if full_map[(i,y)] >= height:
            seen[0] = 0
    for i in range(map_size_x - 1, x, -1):
        if full_map[(i,y)] >= height:
            seen[1] = 0
    for i in range(0, y):
        if full_map[(x,i)] >= height:
            seen[2] = 0
    for i in range(map_size_y - 1, y, -1):
        if full_map[(x,i)] >= height:
            seen[3] = 0
    return max(seen)

def get_scenic_score(x, y, full_map, map_size_x, map_size_y):
    height = full_map[(x,y)]
    seen = [0, 0, 0, 0]
    for i in range(x - 1, -1, -1):
        seen[0] += 1
        if full_map[(i,y)] >= height:
            break
    for i in range(x + 1, map_size_x):
        seen[1] += 1
        if full_map[(i,y)] >= height:
            break
    for i in range(y - 1, -1, -1):
        seen[2] += 1
        if full_map[(x,i)] >= height:
            break
    for i in range(y + 1, map_size_y):
        seen[3] += 1
        if full_map[(x,i)] >= height:
            break
    return prod(seen)

def part_one(full_map, map_size_x, map_size_y):
    seen = 0
    for y in range(0, map_size_y):
        for x in range(0, map_size_x):
            seen += is_seen(x, y, full_map, map_size_x, map_size_y)
    return seen

def part_two(full_map, map_size_x, map_size_y):
    scores = []
    for y in range(0, map_size_y):
        for x in range(0, map_size_x):
            scores.append(get_scenic_score(x, y, full_map, map_size_x, map_size_y))
    return max(scores)


with open("day8.txt" , "r") as f:
    data = [[int(digit) for digit in list(line.strip())] for line in f.readlines()]

tree_map, map_size_x, map_size_y = generate_map(data)
print("Part One:", part_one(tree_map, map_size_x, map_size_y))
print("Part Two:", part_two(tree_map, map_size_x, map_size_y))
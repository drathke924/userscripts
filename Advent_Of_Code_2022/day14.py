def create_rocklist(data_in):
    rocks = set()
    lines = [[tuple([int(a) for a in point.split(',')]) for point in line.split(' -> ')] for line in data_in]
    for line in lines:
        for i in range(0, len(line) - 1):
            x_start, y_start = line[i]
            x_end, y_end = line[i+1]
            if x_start != x_end:
                for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
                    rocks.add((x,y_start))
            elif y_start != y_end:
                for y in range(min(y_start, y_end), max(y_start, y_end) + 1):
                    rocks.add((x_start,y))
    return rocks
                
def move_down(rocklist, position):
    x, y = position
    if (x, y + 1) in rocklist:
        if (x - 1, y + 1) in rocklist:
            if (x + 1, y + 1) in rocklist:
                return position
            else:
                return (x + 1, y + 1)
        else:
            return (x - 1, y + 1)
    else:
        return (x, y + 1)
    
def part_one(rock_in, start_point):
    rocklist = set(rock_in)
    starting_rocks = len(rocklist)
    deepest_rock = max([y for x, y in rocklist])
    position = start_point
    voided = False
    while not voided:
        if (new_pos := move_down(rocklist,position)) == position:
            rocklist.add(new_pos)
            position = start_point
        else:
            if new_pos[1] >= deepest_rock:
                voided = True
            position = new_pos
    return len(rocklist) - starting_rocks

def part_two(rock_in, start_point):
    rocklist = set(rock_in)
    starting_rocks = len(rocklist)
    deepest_rock = max([y for x, y in rocklist])
    position = start_point
    blocked = False
    while not blocked:
        if (new_pos := move_down(rocklist,position)) == position:
            rocklist.add(new_pos)
            position = start_point
            if new_pos == start_point:
                blocked = True
        else:
            if new_pos[1] >= deepest_rock + 2:
                rocklist.add(new_pos)
                position = start_point
                starting_rocks += 1
            else:
                position = new_pos
    return len(rocklist) - starting_rocks



with open("day14.txt" , "r") as f:
    data = create_rocklist(f.read().split('\n'))

start = (500,0)
print("Part One:", part_one(data, start))
print("Part Two:", part_two(data, start))
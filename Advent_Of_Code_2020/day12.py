def prep_data(data_in):
    return (data_in[0], int(data_in[1:]))

def rotate_waypoint(wp_loc, action, amount):
    if (action == 'R' and amount == 90) or (action == 'L' and amount == 270):
        return (wp_loc[1], -wp_loc[0])
    elif (action == 'L' and amount == 90) or (action == 'R' and amount == 270):
        return (-wp_loc[1], wp_loc[0])
    elif amount == 180:
        return (-wp_loc[0], -wp_loc[1])
    else:
        return wp_loc

def complete_instruction(instruction, loc, wp_loc):
    action = instruction[0]
    amount = instruction[1]
    wp_move = {'N': 0,'E': 90,'S':180,'W':270}
    if action in wp_move.keys():
        wp_loc = move_cardinal(wp_loc, amount, wp_move[action])
    elif action == 'F':
        loc = (wp_loc[0] * amount + loc[0], wp_loc[1] * amount + loc[1])
    else:
        wp_loc = rotate_waypoint(wp_loc, action, amount)
    return loc, wp_loc

def set_direction(action, amount, dir):
    if action == 'R':
        return (dir + amount) % 360
    else:
        return (dir - amount + 360) % 360

def move_cardinal(loc, amount, dir):
    if dir == 0:
        return loc[0], loc[1] + amount
    elif dir == 90:
        return loc[0] + amount, loc[1]
    elif dir == 180:
        return loc[0], loc[1] - amount
    else:
        return loc[0] - amount, loc[1]

def make_move(move, dir, loc):
    action = move[0]
    amount = move[1]
    card = {'N': 0,'E': 90,'S':180,'W':270}
    no_move = ('R', 'L')
    if action in no_move:
        return loc, set_direction(action, amount, dir)
    elif action != "F":
        return move_cardinal(loc, amount, card[action]), dir
    else:
        return move_cardinal(loc, amount, dir), dir

def part_one(data_in):
    # dir (90 = east, 180 = south, 270 = west, 0 = north)
    dir = 90
    loc = (0, 0)
    for move in data_in:
        loc, dir = make_move(move, dir, loc)
    return abs(loc[0]) + abs(loc[1])

def part_two(data_in):
    loc = (0, 0)
    wp_loc = (10, 1)
    for instruction in data_in:
        loc, wp_loc = complete_instruction(instruction, loc, wp_loc)
    return abs(loc[0]) + abs(loc[1])

with open("input12.txt" , "r") as f:
	data = list(map(prep_data, f.read().split("\n")))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
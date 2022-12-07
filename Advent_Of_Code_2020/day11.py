from copy import deepcopy

def is_occupied(seats, x, y, dir_x, dir_y):
    try:
        if not seats[(x + dir_x, y + dir_y)]["seat"]:
            return is_occupied(seats, x + dir_x, y + dir_y, dir_x, dir_y)
        elif seats[(x + dir_x, y + dir_y)]["occupied"]:
            return True
        else:
            return False
    except KeyError:
        return False
    return False

def count_occupied(seats, size_x, size_y):
    total_occupied = 0
    for x in range(0, size_x):
        for y in range(0, size_y):
            if seats[(x, y)]["occupied"]:
                total_occupied += 1
    return total_occupied

def occupied_neighbors(seats, x, y, part_one):
    count = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if x != i or y != j:
                try:
                    if seats[(i, j)]["occupied"] and part_one:
                        count += 1
                    elif not part_one:
                        if is_occupied(seats, x, y, i - x, j - y):
                            count += 1
                except KeyError:
                    pass
    return count

def run_round(seats, size_x, size_y, part_one):
    new_seats = deepcopy(seats)
    
    for y in range(0, size_y):
        for x in range(0, size_x):
            if seats[(x, y)]["seat"]:
                occupied_count = occupied_neighbors(seats, x, y, part_one)
                if part_one:
                    limit = 4
                else:
                    limit = 5
                if (seats[(x, y)]["occupied"] and occupied_count >= limit) or ((not seats[(x, y)]["occupied"]) and occupied_count == 0):
                    new_seats[(x, y)]["occupied"] = not seats[(x, y)]["occupied"]
    return new_seats

def build_seating_chart(data_in):
    seats = {}
    size_y = len(data_in)
    for y in range(0, len(data_in)):
        row = list(data_in[y])
        size_x = len(row)
        for x in range(0, len(row)):
            if row[x] == "L":
                seat = True
            else:
                seat = False
            seats[(x, y)] = {"occupied": False, "seat": seat}
    return seats, size_x, size_y

def run_sim(data_in, part_one):
    count = 0
    seats, size_x, size_y = build_seating_chart(data_in)
    new_seats = run_round(seats, size_x, size_y, part_one)
    while new_seats != seats:
        count += 1
        seats = new_seats
        new_seats = run_round(seats, size_x, size_y, part_one)
    return count_occupied(new_seats, size_x, size_y)
    


with open("input11.txt" , "r") as f:
	data = f.read().split("\n")

print("Part One: " + str(run_sim(data,True)))
print("Part Two: " + str(run_sim(data,False)))
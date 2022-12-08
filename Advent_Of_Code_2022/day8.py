def generate_map(data_in):
    map_out = {}
    rows_out = []
    columns_out = []
    for y in range(0, len(data_in)):
        for x in range(0, len(data_in[y])):
            current_num = data_in[y][x]
            if y == 0:
                columns_out.append([current_num])
            else:
                columns_out[x].append(current_num)
            if x == 0:
                rows_out.append([current_num])
            else:
                rows_out[y].append(current_num)
            map_out[(x, y)] = False
    return rows_out, columns_out, map_out

def part_one(rows_in, columns_in, full_map):
    seen = 0
    for y in range(0, len(rows_in)):
        tallest = -1
        for x in range(0, len(rows_in[y])):
            i = rows_in[y][x]
            if i > tallest:
                tallest = i
                if not full_map[(x,y)]:
                    seen += 1
                    full_map[(x,y)] = True
                print(i,end='')
        print(' - ',end='')
        tallest = -1
        for x in range(len(rows_in[y]) - 1, -1, -1):
            i = rows_in[y][x]
            if i > tallest:
                tallest = i
                if not full_map[(x,y)]:
                    seen += 1
                    full_map[(x,y)] = True
                print(i,end='')
        print(rows_in[y])
    for x in range(0, len(columns_in)):
        tallest = -1
        for y in range(0, len(columns_in[x])):
            i = columns_in[x][y]
            if i > tallest:
                tallest = i
                if not full_map[(x,y)]:
                    seen += 1
                    full_map[(x,y)] = True
                print(i, end='')
        print(' - ',end='')
        tallest = -1
        for y in range(len(columns_in[x]) - 1, -1, -1):
            i = columns_in[x][y]
            if i > tallest:
                tallest = i
                if not full_map[(x,y)]:
                    seen += 1
                    full_map[(x,y)] = True
                print(i,end='')
        print(columns_in[x])
    return seen


with open("day8.txt" , "r") as f:
    data = [[int(digit) for digit in list(line.strip())] for line in f.readlines()]

rows, columns, full_map = generate_map(data)
print("Part One:", part_one(rows, columns, full_map))
def part_one(data_in):
    checks =[20,60,100,140,180,220]
    signal_strength = 0
    x = 1
    cycles = 1
    i = 0
    calculating = False
    while cycles < checks[-1]:
        if not calculating:
            if data_in[i][0] == 'noop':
                cycles += 1
            elif data_in[i][0] == 'addx':
                cycles += 1
                calculating = True
                to_add = int(data_in[i][1])
            i += 1
        else:
            calculating = False
            cycles += 1
            x += to_add
        if cycles in checks:
            signal_strength += x * cycles
    return signal_strength

def part_two(data_in):
    screen = [[' ' for i in range(40)] for j in range(6)]
    x = 1
    cycles = 1
    i = 0
    calculating = False
    while cycles < 240:
        pixel_pos = cycles - 1
        if pixel_pos % 40 - 1 <= x <= (pixel_pos + 1) % 40:
            screen[pixel_pos//40][pixel_pos%40] = '#'
        if not calculating:
            if data_in[i][0] == 'noop':
                cycles += 1
            elif data_in[i][0] == 'addx':
                cycles += 1
                calculating = True
                to_add = int(data_in[i][1])
            i += 1
        else:
            calculating = False
            cycles += 1
            x += to_add
    return "\n".join(["".join(line) for line in screen])

with open("day10.txt" , "r") as f:
    data = [line.strip().split() for line in f.readlines()]

print("Part One:",part_one(data))
print("Part Two:", '\n' + part_two(data))
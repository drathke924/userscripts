def prep_data(data_in):
    raw_instruct = data_in.split()
    instruction = [raw_instruct[0], int(raw_instruct[1])]
    return instruction

def switch(curr, accu, instruct):
    comm = instruct[0]
    value = instruct[1]
    if comm == "nop":
        curr += 1
    elif comm == "acc":
        accu += value
        curr += 1
    elif comm == "jmp":
        curr += value
    return curr, accu

def check_loop(data_in):
    acc = 0
    current = 0
    used = set()
    loops = False
    while current not in used and current != len(data_in):
        used.add(current)
        current, acc = switch(current, acc, data[current])
    if current in used:
        loops = True
    return (acc, loops)
    

def part_one(data_in):
    acc = 0
    current = 0
    used = set()
    while current not in used:
        used.add(current)
        current, acc = switch(current, acc, data_in[current])
    return acc

def part_two(data_in):
    loops = True
    revert = list(data_in[0])
    to_change = 1
    while loops:
        result, loops = check_loop(data_in)
        if loops:
            data_in[to_change - 1] = revert
            revert = list(data_in[to_change])
            if data_in[to_change][0] == 'nop':
                data_in[to_change][0] = 'jmp'
            elif data_in[to_change][0] == 'jmp':
                data_in[to_change][0] = 'nop'
            to_change += 1
        else:
            return result


with open("input8.txt" , "r") as f:
	data = list(map(prep_data, f.read().split("\n")))

print("Part One: " + str(part_one(data)))
print("Part Two: " + str(part_two(data)))
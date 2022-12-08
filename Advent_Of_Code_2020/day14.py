import re

def bifurcate(mems_list, floating):
    out_list = []
    for mem in mems_list:
        mem[floating[0]] = '1'
        out_list.append(list(mem))
        mem[floating[0]] = '0'
        out_list.append(list(mem))
    if len(floating) == 1:
        return out_list
    else:
        return bifurcate(out_list, floating[1:])

def part_one(data_in):
    memory_space = {}
    mask = []
    mem = 0
    for line in data_in:
        split_line = line.split()
        if split_line[0] == 'mask':
            mask = list(split_line[2])
            mask.reverse()
        else:
            to_write = []
            mem = int(re.search('\d+', split_line[0])[0])
            temp = list(bin(int(split_line[2])))[2:]
            temp.reverse()
            for i in range(0, len(mask)):
                if mask[i] == 'X':
                    if i < len(temp):
                        to_write.append(temp[i])
                    else:
                        to_write.append('0')
                else:
                    to_write.append(mask[i])
            to_write.reverse()
            memory_space[mem] = int("0b" + "".join(to_write), 2)
    return sum(memory_space.values())

def part_two(data_in):
    memory_space = {}
    mask = []
    mem = 0
    for line in data_in:
        split_line = line.split()
        if split_line[0] == 'mask':
            mask = list(split_line[2])
            mask.reverse()
        else:
            floating = []
            to_write = ['0' for i in range(0, 36)]
            mem = int(re.search('\d+', split_line[0])[0])
            temp = list(bin(mem))[2:]
            temp.reverse()
            mems_to_write = []
            for i in range(0, len(mask)):
                if mask[i] == 'X':
                    floating.append(i)
                elif i >= len(temp) or mask[i] == '1':
                    to_write[i] = mask[i]
                else:
                    to_write[i] = temp[i]
            mems_to_write.append(to_write)
            outwrite = bifurcate(mems_to_write, floating)
            for address in outwrite:
                address.reverse()
                memory_space[int("0b" + "".join(address), 2)] = int(split_line[2])
    return sum(memory_space.values())
            

with open("input14.txt" , "r") as f:
	data = f.read().split("\n")

print("Part One:", part_one(data))
print("Part Two:", part_two(data))
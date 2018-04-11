from gmpy2 import is_prime

with open("day23.txt", "r") as f:
    DATA = f.read().splitlines()

DATA = list(map(lambda x: x.split(" "), DATA))

def get(instr, reg):
    try:
        return int(instr)
    except ValueError:
        return reg[instr]
def reg_init():
    global DATA
    regset = {}
    for l in DATA:
        if l[1].isalpha() and l[1] not in regset.keys():
            regset[l[1]] = 0
        if l[2].isalpha() and l[2] not in regset.keys():
            regset[l[2]] = 0
    return regset

def part_one():
    global DATA
    count = 0
    regset = reg_init()
    step = 0
    lastsound = 0
    while step < len(DATA):
        instruct = list(DATA[step])
        #print(str(instruct) + " " + str(regset))
        if instruct[0] == "set":
            regset[instruct[1]] = get(instruct[2], regset)
        elif instruct[0] == "sub":
            regset[instruct[1]] -= get(instruct[2], regset)
        elif instruct[0] == "mul":
            count += 1
            regset[instruct[1]] *= get(instruct[2], regset)
        elif instruct[0] == "jnz":
            if get(instruct[1], regset) != 0:
                step += get(instruct[2], regset)
                continue
        step += 1
    return count

def part_two():
    count = 0
    for i in range(106500, 123501, 17):
        if not is_prime(i):
            count += 1
    return count

print(part_one())
print(part_two())

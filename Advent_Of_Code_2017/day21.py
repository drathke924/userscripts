from math import sqrt

with open("day21data.txt", "r") as f:
    DATA = f.read().splitlines()

for i in range(len(DATA)):
    DATA[i] = DATA[i].split(" ")

RULEDICT = {}

for l in DATA:
    RULEDICT[l[0]] = l[2]



start = ".#./..#/###"
#start = "#..#/..../#..#/.##."

def transpose(inp):
    out = []
    inp = inp.split("/")
    for i in range(len(inp)):
        out.append("")
    for i in range(len(inp)):
        for j in range(len(inp)):
            out[j] += inp[len(inp) - 1 - i][len(inp) - 1 - j]
    return "/".join(out)

def vFlip(inp):
    return "/".join(inp.split("/")[::-1])

def check(inp):
    global RULEDICT
    doH = True
    count = 0
    while count < 20:
        if inp in RULEDICT.keys():
            return RULEDICT[inp]
        elif doH:
            inp = transpose(inp)
            doH = False
        else:
            inp = vFlip(inp)
            doH = True
        count += 1


def div(inp):
    out = []
    size = len(inp.split("/")[0])
    if size == 2 or size == 3:
        return [inp]
    elif size % 2 == 0:
        temp = inp.split("/")
        for i in range(0, size, 2):
            for j in range(0, size, 2):
                smalltemp = []
                for k in range(2):
                    smalltemp.append(temp[i + k][j:j+2])
                out.append("/".join(smalltemp))
        return out
    elif size % 3 == 0:
        temp = inp.split("/")
        for i in range(0, size, 3):
            for j in range(0, size, 3):
                smalltemp = []
                for k in range(3):
                    smalltemp.append(temp[i + j + k][j:j+3])
                out.append("/".join(smalltemp))
        return out

def linejoin(inp):
    out = []
    size = int(sqrt(len(inp)))
    if size > 1:
        for i in range(len(inp)):
            inp[i] = inp[i].split("/")
        insize = len(inp[0])
        for i in range(size):
            lines = []
            for k in range(insize):
                lines.append("")
            for j in range(insize):
                for k in range(size):
                    ind = k + (i*2)
                    lines[j] = lines[j] + inp[ind][j]
            out.append("/".join(lines))
    else:
        out = inp
    #print(out)
    return "/".join(out)



output = div(start)
for i in range(5):
    output = div(linejoin(output))
    for j in range(len(output)):
        output[j] = check(output[j])
print(linejoin(output).count("#"))

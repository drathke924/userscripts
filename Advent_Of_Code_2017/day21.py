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
        out.append(list(inp[i]))
    out = list(map("".join, zip(*out)))
    #print(out)
    return "/".join(out)

def vFlip(inp):
    return "/".join(inp.split("/")[::-1])

def check(inp):
    global RULEDICT
    doH = True
    count = 0
    while count < 20:
        if inp in RULEDICT.keys():
            #print(str(inp) + " " + str(RULEDICT[inp]))
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
        #print(out)
        return out
    elif size % 3 == 0:
        temp = inp.split("/")
        for i in range(0, size, 3):
            for j in range(0, size, 3):
                smalltemp = []
                for k in range(3):
                    smalltemp.append(temp[i + k][j:j+3])
                out.append("/".join(smalltemp))
        #print(out)
        return out

def linejoin(inp):
    out = []
    size = int(sqrt(len(inp)))
    #print(inp)
    temp = list(inp)
    if size > 1:
        for i in range(len(inp)):
            temp[i] = temp[i].split("/")
        insize = len(temp[0])
        for i in range(size):
            lines = []
            for k in range(insize):
                lines.append("")
            for j in range(insize):
                for k in range(size):
                    ind = k + i * size
                    #print(str(temp[ind]) + " " + str(ind) + " " + str(i) + " " + str(k) + " " + str(j) + " " + str(insize))
                    lines[j] = lines[j] + temp[ind][j]
            out.append("/".join(lines))
    else:
        out = list(inp)
    #print(out)
    return "/".join(out)



output = div(start)
for i in range(5):
    output = div(linejoin(output))
    for j in range(len(output)):
        output[j] = check(output[j])
#print(linejoin(output))
print(linejoin(output).count("#"))
for i in range(13):
    output = div(linejoin(output))
    for j in range(len(output)):
        output[j] = check(output[j])
print(linejoin(output).count("#"))

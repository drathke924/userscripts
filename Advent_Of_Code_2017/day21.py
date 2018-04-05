from math import sqrt

with open("day21test.txt", "r") as f:
    DATA = f.read().splitlines()

for i in range(len(DATA)):
    DATA[i] = DATA[i].split(" ")

RULEDICT = {}

for l in DATA:
    RULEDICT[l[0]] = l[2]



start = ".#./..#/###"
#start = "#..#/..../#..#/.##."

def hFlip(inp):
    out = []
    for s in inp.split("/"):
        out.append(s[::-1])
    return "/".join(out)

def vFlip(inp):
    return "/".join(inp.split("/")[::-1])

def check(inp):
    global RULEDICT
    doH = True
    while True:
        if inp in RULEDICT.keys():
            return RULEDICT[inp]
        elif doH:
            inp = hFlip(inp)
            doH = False
        else:
            inp = vFlip(inp)
            doH = True


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
    size = sqrt(len(inp))
    if size > 1:
        for i in range(len(inp)):
            inp[i] = inp[i].split("/")
        for i in range(size):
            for j in range(size):
                insize = len(inp[j + (i*2)])
                for k in range(insize):
                    

    out = list(inp)
    print(out)
    return "/".join(out)



output = div(start)
#print(output)
#print(linejoin(output))
for i in range(2):
    for j in range(len(output)):
        #print(check(output[j]))
        output[j] = check(output[j])
    #print(output)
    output = div(linejoin(output))
#print(linejoin(output))

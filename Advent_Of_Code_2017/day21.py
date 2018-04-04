with open("day21test.txt", "r") as f:
    DATA = f.read().splitlines()

for i in range(len(DATA)):
    DATA[i] = DATA[i].split(" ")

DATADICT = {}

for l in DATA:
    DATADICT[l[0]] = l[2]



start = ".#./..#/###"

def hFlip(inp):
    out = []
    for s in inp.split("/"):
        out.append(s[::-1])
    return "/".join(out)

def vFlip(inp):
    return "/".join(inp.split("/")[::-1])

def check(inp):
    global DATA
    doH = True
    while True:
        if inp in DATADICT.keys():
            return DATADICT[inp]
        elif doH:
            inp = hFlip(inp)
            doH = False
        else:
            inp = vFlip(inp)
            doH = True

print(check(start))
#for i in range(2):

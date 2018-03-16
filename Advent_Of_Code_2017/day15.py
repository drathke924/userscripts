a = 722
b = 354

afactor = 16807
bfactor = 48271

def generatorA():
	

def generatorB():
	
matchcount = 0

for i in range(40000000):
	a = (a * afactor) % 2147483647
	b = (b * bfactor) % 2147483647
	if bin(a)[2:].zfill(16)[-16:] == bin(b)[2:].zfill(16)[-16:]:
		matchcount += 1

print(matchcount)
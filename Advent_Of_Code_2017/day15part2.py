a = 722
b = 354

afactor = 16807
bfactor = 48271

def generatorA(x):
	x = (x * afactor) % 2147483647
	while x % 4 != 0:
		x = (x * afactor) % 2147483647
	return x

def generatorB(x):
	x = (x * bfactor) % 2147483647
	while x % 8 != 0:
		x = (x * bfactor) % 2147483647
	return x
	
matchcount = 0

for i in range(5000000):
	if i % 100000 == 0:
		print(i/1000000)
	a = generatorA(a)
	b = generatorB(b)
	if bin(a)[2:].zfill(16)[-16:] == bin(b)[2:].zfill(16)[-16:]:
		matchcount += 1

print(matchcount)
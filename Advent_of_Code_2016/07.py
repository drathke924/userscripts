import re

with open ("07.txt", 'r') as f:
	data = f.read().splitlines()

def abba(word):
	return any(a == d and b == c and a != b for a, b, c, d in zip(word, word[1:], word[2:], word[3:])) #courtesy of u/barnybug

def aba(word):
	out = []
	for a, b, c in zip(word, word[1:], word[2:]):
		if a == c and a != b:
			out.append(a+b+c)
	return out

outside = re.compile(r"(?:\w+\[)|(?:\]\w+\[)|(?:\]\w+)")
inside = re.compile(r"(?:\w+\])|(?:\[\w+\])|(?:\[\w+)")

def partOne(data):
	total = 0
	allsupport = 0
	for line in data:
		supported = False
		for out in outside.findall(line):
			if abba(out):
				supported = True
		for ins in inside.findall(line):
			if abba(ins):
				supported = False
		if supported:
			allsupport += 1
		total += 1
	return allsupport

def partTwo(data):
	allsupport = 0
	for line in data:
		supported = False
		for out in outside.findall(line):
			for ins in inside.findall(line):
				for test in aba(out):
					test = test[1] + test[0] + test[1]
					if test in aba(ins):
						supported = True
		if supported:
			allsupport += 1
	return allsupport

print(partOne(data))
print(partTwo(data))
	
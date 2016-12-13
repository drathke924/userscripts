import re

allsupport = 0
total = 0

with open ("advent7.txt", 'r') as f:
	data = f.read().splitlines()

def abba(word):
	return any(a == d and b == c and a != b for a, b, c, d in zip(word, word[1:], word[2:], word[3:])) #courtesy of u/barnybug

outside = re.compile(r"(?:\w+\[)|(?:\]\w+\[)|(?:\]\w+)")
inside = re.compile(r"(?:\w+\])|(?:\[\w+\])|(?:\[\w+)")

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

print(allsupport)
print(total)
	
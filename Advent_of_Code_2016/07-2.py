import re

allsupport = 0

with open ("advent7.txt", 'r') as f:
	data = f.read().splitlines()

def aba(word):
	out = []
	for a, b, c in zip(word, word[1:], word[2:]):
		if a == c and a != b:
			out.append(a+b+c)
	return out

outside = re.compile(r"(?:\w+\[)|(?:\]\w+\[)|(?:\]\w+)")
inside = re.compile(r"(?:\w+\])|(?:\[\w+\])|(?:\[\w+)")

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

print(allsupport)
	
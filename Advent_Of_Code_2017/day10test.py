start = []
for i in range(256):
	start.append(i)

result = start

input = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
skip = 0

tracker = 0

for length in input:
	sublist = result[:length]
	result = sublist[::-1] + result[length:]
	sublist = result[:(length + skip) % len(result)]
	result = result[(length + skip) % len(result):] + sublist
	tracker += length + skip
	skip += 1

if tracker % len(result) != 0:
	print(result[(tracker % len(result)) - 1:] + result[:(tracker % len(result)) - 1])
else:
	print(result)
discs = [(17, 5), (19, 8), (7, 1), (13, 7), (5, 1), (3, 0)]
time = 0
part2 = False
if part2:
	discs.append((11, 0))

dropped = False

while not dropped:
	dropped = True
	for i, disc in enumerate(discs):
		if ((disc[1] + time + i + 1) % disc[0]) != 0:
			dropped = False
			break
	time += 1

print(time - 1)


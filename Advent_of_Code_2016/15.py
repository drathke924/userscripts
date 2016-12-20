discs = [(17, 15), (3, 2), (19, 4), (13, 2), (7, 2), (5, 0)]
time = 0
part2 = True
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


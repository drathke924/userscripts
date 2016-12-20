from operator import itemgetter

ranges = []

with open("20.txt", "r") as f:
	data = f.read().splitlines()

for i in data:
	i = i.split("-")
	ranges.append((int(i[0]), int(i[1])))

ranges = sorted(ranges, key=itemgetter(0))

unblocked = []
i = 0
while i < 4294967295:
	blocked = False
	for j in ranges:
		if i >= j[0] and i <= j[1]:
			blocked = True
			i = j[1]
			break
	if not blocked:
		unblocked.append(i)
	i += 1

print(sorted(unblocked)[0])
print(len(unblocked))




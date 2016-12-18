from time import clock

start_time = clock()
data = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"

def isTrap(last, index):
	if index < 1:
		if last[index + 1] == "^":
			return True
	elif index > len(last) - 2:
		if last[index - 1] == "^":
			return True
	else:
		if last[index - 1] != last[index + 1]:
			return True
	return False


def traps(floor, n):
	rows = [floor]
	safe = 0

	for i in range(n - 1):
		current = ""
		for j in range(len(floor)):
			if isTrap(rows[i], j):
				current += "^"
			else:
				current += "."
		rows.append(current)

	for i in rows:
		safe += i.count(".")

	return safe


print(traps(data, 40))
print(clock() - start_time)

lap_time = clock()
print(traps(data, 399999))
print(clock() - lap_time)
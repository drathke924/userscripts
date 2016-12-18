from time import clock

start_time = clock()
data = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"

def traps(floor, n):
	rows = [floor]
	safe = 0

	for i in range(n - 1):
		current = ""
		for j in range(len(floor)):
			if j < 1:
				if rows[i][j + 1] == "^":
					current += "^"
				else:
					current += "."
			elif j > len(floor) - 2:
				if rows[i][j - 1] == "^":
					current += "^"
				else:
					current += "."
			else:
				if rows[i][j - 1] != rows[i][j + 1]:
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
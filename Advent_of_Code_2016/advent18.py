data = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"

rows = []

safe = 0

rows.append(data)

for i in range(399999):
	current = ""
	for j in range(len(data)):
		if j < 1:
			if rows[i][j + 1] == "^":
				current += "^"
			else:
				current += "."
		elif j > len(data) - 2:
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

print(len(rows))

print(safe)


secsum = 0

file = open("04.txt", 'r')
rooms = file.read().splitlines()
file.close() 

def get_checksum(name):
	counts = {}
	for char in name:
		if char not in counts.keys():
			counts[char] = name.count(char)

	check = ""

	while len(check) < 5:
		tempcheck = []
		countsort = sorted(counts, key=counts.get, reverse=True)
		for i, char in enumerate(countsort):
			tempcheck.append(char)
			if i < len(countsort) - 1 and counts[char] == counts[countsort[i+1]]:
				continue
			else:
				check += "".join(sorted(tempcheck))
				tempcheck = []

	return check[0:5]

def shift(c, n):
	if ord(c) > 64 and ord(c) < 91:
		c = chr((((ord(c) - 65) + n) % 26) + 65)
	elif ord(c) > 96 and ord(c) < 123:
		c = chr((((ord(c) - 97) + n) % 26) + 97)
	return c




for room in list(rooms):
	realchecksum = ""

	encrypted = room[0:-11]
	encrypted = encrypted.split('-')
	sector = int(room[-10:-7])
	checksum = room[-6:-1]
	realchecksum = get_checksum("".join(encrypted))
	if realchecksum == checksum:
		secsum += sector
	else:
		rooms.remove(room)

for room in rooms:
	encrypted = room[0:-11]
	sector = int(room[-10:-7])
	decrypted = ""

	for c in encrypted:
		decrypted += shift(c, sector)

	if "pole" in decrypted or "north" in decrypted or "object" in decrypted:
		print(decrypted)
		print(sector)


print(secsum)
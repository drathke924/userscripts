start = "10001001100000001"
test_start = "10000"
disk = ""
checksum = ""

def dragon(data):
	a = data
	b = ""
	reverse = data[::-1]
	for c in reverse:
		if c == "1":
			b += "0"
		else:
			b += "1"
	return a + "0" + b

def check(data):
	while len(data) % 2 == 0:
		pairs = [data[i:i+2] for i in range(0, len(data), 2)]
		data = ""
		for p in pairs:
			if p[0] == p[1]:
				data += "1"
			else:
				data += "0"
	return data



disk = dragon(start)

while len(disk) < 35651584:
	disk = dragon(disk)

disk = disk[:35651584]

checksum = check(disk)

print(disk)
print("---")
print(checksum)

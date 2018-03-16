with open("day13data.txt", "r") as f:
	data = f.read().splitlines()

for i in range(len(data)):
	data[i] = data[i].split()
	data[i] = (int(data[i][0][:-1]), int(data[i][1]))
	
severity = 0
safe = False
wait = 0

for x in data:
	if x[0] % ((x[1] - 1)*2) == 0:
		print(x)
		severity += x[0] * x[1]
		
print(severity)

while not safe:
	caught = False
	for x in data:
		if x[0] + wait >= ((x[1] - 1)*2) and (x[0] + wait) % ((x[1] - 1)*2) == 0:
			caught = True
	if not caught:
		safe = True
	else:
		wait += 1

print(wait)
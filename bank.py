totes = []

steps = 0
inita = 164
initb = -10
a = inita
b = initb
print(a)
print(b)
while 0 < (a + b) <= 1000000:
	steps += 1
	if a + b == 1000000:
		print(a + b)
		print("A: " + str(inita) + " B: " + str(initb) + " Steps: " + str(steps))
		totes.append((inita, initb, steps))
		break
	else:
		steps += 1
		a = a + b
		print(a)
		if a + b == 1000000:
			print(a + b)
			print("A: " + str(inita) + " B: " + str(initb) + " Steps: " + str(steps))
			totes.append((inita, initb, steps))
			break
		elif a + b > 1000000:
			break
		else:
			b = a + b
			print(b)

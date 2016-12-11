def shift(c, n):
	if ord(c) > 64 and ord(c) < 91:
		c = chr((((ord(c) - 65) + n) % 26) + 65)
	elif ord(c) > 96 and ord(c) < 123:
		c = chr((((ord(c) - 97) + n) % 26) + 97)
	return c

print("What is the text?")
text = input()

for i in range(1, 26):
	for j in range(0, len(text)):
		text = text[:j] + shift(text[j], 1) + text[j + 1:]
	print(text)

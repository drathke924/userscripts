import hashlib
from time import time

start_time = time()

salt = "cuanljph"
keys = []
integer = 0
hashes = []
part2 = True
found = False

def stretch(text):
	for i in range(2016):
		hashstretch = hashlib.md5()
		hashstretch.update(text.encode("utf-8"))
		text = hashstretch.hexdigest()
	return text


while len(keys) < 64:
	hashid = salt + str(integer)
	m = hashlib.md5()
	m.update(hashid.encode("utf-8"))
	test = m.hexdigest()
	if part2:
		test = stretch(test)
	for i, c in enumerate(test):
		if i + 3 <= len(test) and c * 3 in test[i:i+3]:
			lasthash = integer
			for hsh in list(hashes):
				if hsh[1] <= integer :
					hashes.remove(hsh)
				else:
					if c * 5 in hsh[0]:
						print(integer)
						keys.append(test)
						print(len(keys))
						found = True
						break
			if found:
				found = False
				break
			if len(hashes) > 0:
				lasthash = hashes[-1][1]
			for n in range(lasthash + 1, integer + 1001):
				newhashid = salt + str(n)
				newhash = hashlib.md5()
				newhash.update(newhashid.encode("utf-8"))
				newtest = newhash.hexdigest()
				if part2:
					newtest = stretch(newtest)
				hashes.append((newtest, n))
				if c * 5 in newtest:
					print(integer)
					keys.append(test)
					print(len(keys))
					break
			break

	integer += 1

print(time() - start_time)
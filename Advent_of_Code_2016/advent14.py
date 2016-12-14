import hashlib
from time import time
from collections import deque

start_time = time()

salt = "cuanljph"
keys = []
integer = 0
end = 1000
hashes = deque()
part2 = True
found = False

def stretch(text):
	for i in range(2016):
		hashstretch = hashlib.md5()
		hashstretch.update(text.encode("utf-8"))
		text = hashstretch.hexdigest()
	return text

for i in range(0, end):
	hashid = salt + str(i)
	hash = hashlib.md5()
	hash.update(hashid.encode("utf-8"))
	test = hash.hexdigest()
	if part2:
		test = stretch(test)
	hashes.append((test, i))



while len(keys) < 64:
	hashid = salt + str(integer)
	m = hashlib.md5()
	m.update(hashid.encode("utf-8"))
	test = m.hexdigest()
	if part2:
		test = stretch(test)

	hashid_2 = salt + str(end)
	hash_2 = hashlib.md5()
	hash_2.update(hashid_2.encode("utf-8"))
	test_2 = hash_2.hexdigest()
	if part2:
		test_2 = stretch(test_2)

	hashes.popleft()
	hashes.append((test_2, end))

	for i, c in enumerate(test):
		if i + 3 <= len(test) and c * 3 in test[i:i+3]:
			for hsh in hashes:
				if c * 5 in hsh[0]:
					keys.append(test)
					break
			break

	integer += 1
	end += 1

print(integer - 1)
print(time() - start_time)
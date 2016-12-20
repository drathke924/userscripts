import hashlib

doorid = input()
password = ""
integer = 0



for x in range(8):
	test = "xxxxx"
	
	while test[0:5] != "00000":
		hashid = doorid + str(integer)
		m = hashlib.md5()
		m.update(hashid.encode("utf-8"))
		test = m.hexdigest()
		integer += 1
		if test[0:5] == "00000":
			password += test[5]
			print(password)


print(password)
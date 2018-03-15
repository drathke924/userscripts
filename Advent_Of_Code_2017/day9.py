with open("day9data.txt", "r") as f:
	data = f.read()

dex = 0
garcount = 0

def score(level):
	global data
	global dex
	global garcount
	ignore = False
	garbage = False
	endlevel = level
	while dex < len(data) - 1:
		dex += 1
		#print(str(ignore) + " " + str(garbage))
		#print(str(data[dex]) + " " + str(dex) + " " + str(endlevel))
		if not ignore and not garbage:
			if data[dex] == '<':
				garbage = True
			elif data[dex] == '{':
				#print(str(level) + " " + str(dex))
				endlevel += score(level + 1)
			elif data[dex] == '}':
				return endlevel
		elif not ignore:
			if data[dex] == '!':
				ignore = True
			elif data[dex] == '>':
				garbage = False
			else:
				garcount += 1
		else:
			ignore = False
		#print(endlevel)
	return endlevel
	

print(score(1))
print(garcount)
start = []
for i in range(256):
	start.append(i)

stringinput = "hfdlxzhv"
kicker = [17, 31, 73, 47, 23]
map = []

def knot(inlist, rounds, input):
	position = 0
	skip = 0
	inlist = list(inlist)
	for i in range(rounds):
		for length in input:
			prelist = []
			midlist = []
			postlist = []
			endlist = []
			fliplist = []
			#find the position of the last item in the subset of items to be reversed
			subpos = position + length - len(inlist)
			if subpos > 0:
				#create sublist for items from the beginning of the main list to the last item to be reversed
				prelist = inlist[:subpos]
			#create sublist for items from the position of the start of the items to be reversed up to either the end of the list or the last item to be reversed, whichever comes first
			postlist = inlist[position:min(position + length, len(inlist))]
			if position + length < len(inlist):
				#create a sublist for anything at the end of the main list that wasn't grabbed by the postlist
				endlist = inlist[min(position + length, len(inlist)):]
			if len(prelist) + len(postlist) < len(inlist):
				#create a sublist for anything between the prelist and postlist
				midlist = inlist[len(prelist):(len(inlist) - (len(postlist) + len(endlist)))]
			#create the list of items to be reversed in the order you'd find them in the main list and reverse them
			fliplist = postlist + prelist
			fliplist = fliplist[::-1]
			#break the list back into its constituent pieces
			prelist = fliplist[len(postlist):]
			postlist = fliplist[:len(postlist)]
			#put all the sublists back together
			inlist = prelist + midlist + postlist + endlist
			position = (position + length + skip) % len(inlist)
			skip += 1
	return inlist
	
def listToHash(inlist):
	newlist = []
	for i in range(16):
		toadd = inlist.pop(0)
		for j in range(15):
			toadd = toadd ^ inlist.pop(0)
		newlist.append(toadd)

	outstring = ""
	for x in newlist:
		temp = str(hex(x))[-2:]
		if temp[0] == "x":
			temp = "0" + temp[1]
		outstring += temp
	
	return outstring
	
def stringToList(instring):
	listout = []
	for c in instring:
		listout.append(ord(c))
	return listout

def hashToBin(stringin):
	temp = ""
	stringout = ""
	leadingzeros = 0
	for c in stringin:
		temp = bin(int("0x" + c, 16))
		leadingzeros = 4 - (len(temp) - 2)
		stringout += "0" * leadingzeros + temp[2:]
	return stringout

def usedNeighbors(coord, grp):
	global map
	nbr = []
	x = coord[0]
	y = coord[1]
	if x > 0:
		if map[y][x - 1] == "1":
			nbr.append((x - 1, y))
	if y > 0:
		if map[y - 1][x] == "1":
			nbr.append((x, y - 1))
	if y < 127:
		if map[y + 1][x] == "1":
			nbr.append((x, y + 1))
	if x < 127:
		if map[y][x + 1] == "1":
			nbr.append((x + 1, y))
	return nbr
	
def groupUp(coord, grp):
	grp.append(coord)
	for xy in usedNeighbors(coord, grp):
		if xy not in grp:
			groupUp(xy, grp)
	return grp

for i in range(128):
	map.append(hashToBin(listToHash(knot(start, 64, stringToList(stringinput + "-" + str(i)) + kicker))))

used = 0
for s in map:
	used += s.count("1")

checked = []
groupcount = 0

for x in range(128):
	for y in range(128):
		if map[y][x] == "1" and (x, y) not in checked:
			checked += groupUp((x, y), [])
			groupcount += 1

print(used)
print(groupcount)
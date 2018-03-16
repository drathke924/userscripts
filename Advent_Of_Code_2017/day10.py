start = []
for i in range(256):
	start.append(i)

result = start

listinput = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
stringinput = "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"
kicker = [17, 31, 73, 47, 23]
skip = 0
position = 0
listlen = len(result)

def knot(inlist, rounds, input):
	global position
	global skip
	inlist = list(inlist)
	for i in range(rounds):
		for length in input:
			prelist = []
			midlist = []
			postlist = []
			endlist = []
			fliplist = []
			#find the position of the last item in the subset of items to be reversed
			subpos = position + length - listlen
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

partone = knot(start, 1, listinput)

position = 0
skip = 0
listinput = []

for c in stringinput:
	listinput.append(ord(c))
	
listinput = listinput + kicker

parttwolist = knot(start, 64, listinput)
newlist = []
for i in range(16):
	toadd = parttwolist.pop(0)
	for j in range(15):
		toadd = toadd ^ parttwolist.pop(0)
	newlist.append(toadd)

outstring = ""
for x in newlist:
	temp = str(hex(x))[-2:]
	if temp[0] == "x":
		temp = "0" + temp[1]
	outstring += temp

print(partone[0] * partone[1])
print(outstring)
	


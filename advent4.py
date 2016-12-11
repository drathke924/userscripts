

secsum = 0

file = open("advent4.txt", 'r')
rooms = file.read().splitlines()
file.close() 

for room in rooms:
	realchecksum = ""

	encrypted = room[0:-11]
	encrypted = encrypted.split('-')
	sector = int(room[-10:-7])
	checksum = room[-6:-1]

	
	
	
	



	
	


print(secsum)
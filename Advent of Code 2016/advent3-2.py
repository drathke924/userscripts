possible = 0
allem = 0

file = open("advent3.txt", 'r')
triangles = file.read().splitlines()
file.close() 

for i in range(len(triangles)):
	triangles[i] = [int(x) for x in triangles[i].split()]
for i in range(0, int(len(triangles)/3)):
	allem += 3
	row = i * 3
	triuno = [triangles[row][0], triangles[row + 1][0], triangles[row + 2][0]]
	tridos = [triangles[row][1], triangles[row + 1][1], triangles[row + 2][1]]
	tritre = [triangles[row][2], triangles[row + 1][2], triangles[row + 2][2]]
	print(triuno)
	print(tridos)
	print(tritre)
	triuno.sort()
	tridos.sort()
	tritre.sort()
	
	if triuno[0] + triuno[1] > triuno[2]:
		possible += 1
	if tridos[0] + tridos[1] > tridos[2]:
		possible += 1
	if tritre[0] + tritre[1] > tritre[2]:
		possible += 1

print(possible)
print(allem)
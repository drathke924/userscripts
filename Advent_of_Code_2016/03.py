possible = 0

file = open("03.txt", 'r')
triangles = file.read().splitlines()
file.close() 

def partOne(triangles):
	possible = 0
	for triangle in triangles:
		triangle = [int(x) for x in triangle.split()]
		triangle.sort()
		if triangle[0] + triangle[1] > triangle[2]:
			possible += 1
	return possible

def partTwo(triangles):
	possible = 0
	for i in range(len(triangles)):
		triangles[i] = [int(x) for x in triangles[i].split()]
	for i in range(0, int(len(triangles)/3)):
		row = i * 3
		triuno = [triangles[row][0], triangles[row + 1][0], triangles[row + 2][0]]
		tridos = [triangles[row][1], triangles[row + 1][1], triangles[row + 2][1]]
		tritre = [triangles[row][2], triangles[row + 1][2], triangles[row + 2][2]]
		triuno.sort()
		tridos.sort()
		tritre.sort()
		if triuno[0] + triuno[1] > triuno[2]:
			possible += 1
		if tridos[0] + tridos[1] > tridos[2]:
			possible += 1
		if tritre[0] + tritre[1] > tritre[2]:
			possible += 1
	return possible

print(partOne(triangles))
print(partTwo(triangles))
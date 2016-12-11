possible = 0
allem = 0

file = open("advent3.txt", 'r')
triangles = file.read().splitlines()
file.close() 

for triangle in triangles:
	allem += 1
	triangle = [int(x) for x in triangle.split()]
	triangle.sort()
	if triangle[0] + triangle[1] > triangle[2]:
		possible += 1

print(possible)
print(allem)
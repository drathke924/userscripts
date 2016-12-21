from itertools import combinations

nums = [2, 3, 4]

target = 6

for i in combinations(nums, 2):
	if sum(i) == target:
		print( [nums.index(i[0]), nums.index(i[1])] )
with open("day1.txt" , "r") as f:
    data = f.readlines()

elves = [0]
index = 0

for line in data:
    try:
        elves[index] += int(line.strip())
    except ValueError:
        index += 1
        elves.append(0)

elves.sort(reverse=True)

part1 = elves[0]
part2 = sum(elves[0:3])

print("Part One: " + str(part1))
print("Part Two: " + str(part2))
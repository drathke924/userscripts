with open("day3.txt" , "r") as f:
    data = f.readlines()

part1 = 0
part2 = 0

for ruck in data:
    clean_ruck = list(ruck.strip())
    pocket1 = clean_ruck[0:int(len(clean_ruck)/2)]
    pocket2 = clean_ruck[int(len(clean_ruck)/2):]
    shared = str(list(set(pocket1).intersection(pocket2))[0])
    if shared.isupper():
        part1 += ord(shared) - 38
    else:
        part1 += ord(shared) - 96

for i in range(0, len(data), 3):
    ruck1 = list(data[i].strip())
    ruck2 = list(data[i + 1].strip())
    ruck3 = list(data[i + 2].strip())
    badge = str(list(set(ruck1).intersection(ruck2).intersection(ruck3))[0])
    if badge.isupper():
        part2 += ord(badge) - 38
    else:
        part2 += ord(badge) - 96

print("Part One: " + str(part1))
print("Part Two: " + str(part2))
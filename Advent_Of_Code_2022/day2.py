with open("day2.txt" , "r") as f:
    data = f.readlines()


part1 = 0
part2 = 0

def part1_results(data_in):
    guide = {"X": (1, "C", "A"), "Y": (2, "A", "B"), "Z": (3, "B", "C")}
    results = 0
    results += guide[data_in[1]][0]
    if data_in[0] == guide[data_in[1]][2]:
        results += 3
    elif data_in[0] == guide[data_in[1]][1]:
        results += 6
    return results

def part2_results(data_in):
    guide = {"A": (3, 1, 2), "B": (1, 2, 3), "C": (2, 3, 1)}
    results = 0
    win_lose = ord(data_in[1]) - 88
    results += win_lose*3
    results += guide[data_in[0]][win_lose]
    return results


for round in data:
    round_data = round.split()
    part1 += part1_results(round_data)
    part2 += part2_results(round_data)



print("Part One: " + str(part1))
print("Part Two: " + str(part2))
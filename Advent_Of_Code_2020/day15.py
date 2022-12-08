starting_numbers = [6,3,15,13,1,0]

def memory_game(data_in, turns):
    spoken = {}
    for i in range(0, turns):
        if i < len(data_in):
            next_num = data_in[i]
        else:
            if last_num not in spoken.keys():
                next_num = 0
            else:
                next_num = i - spoken[last_num]
        if i != 0:
            spoken[last_num] = i
        last_num = next_num
    return last_num
        

print("Part One:", memory_game(starting_numbers, 2020))
print("Part Two:", memory_game(starting_numbers, 30000000))

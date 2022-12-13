import ast
from copy import deepcopy

def check_order(item_one, item_two):
    try:
        x = 0
        y = 0
        while x == y:
            test, test2 = item_one[0], item_two[0]
            x = item_one.pop(0)
            y = item_two.pop(0)
        if isinstance(x, list) and isinstance(y, list):
            check = check_order(x, y)
            return check if check != None else check_order(item_one[1:], item_two[1:]) 
        if x < y:
            return True
        elif x > y:
            return False
        else:
            return check_order(x, y)
    except TypeError:
        if isinstance(x, list):
            check = check_order(x, [y])
            return check if check != None else check_order(item_one[1:], item_two[1:]) 
        elif isinstance(y, list):
            check = check_order([x], y)
            return check if check != None else check_order(item_one[1:], item_two[1:]) 
    except IndexError:
        if len(item_one) == 0 and len(item_two) == 0:
            return None
        elif len(item_one) == 0:
            return True
        elif len(item_two) == 0:
            return False
    return False

def part_one(data_in):
    count = 0
    index = 1
    for pair in data_in:
        a, b = [ast.literal_eval(x) for x in pair.split('\n')]
        if check_order(a, b):
            count += index
        index += 1
    return count

def part_two(data_in):
    in_order = False
    corrected = {}
    index = 1
    for pair in data_in:
        a, b = [ast.literal_eval(x) for x in pair.split('\n')]
        corrected[index] = a
        index += 1
        corrected[index] = b
        index += 1
    while not in_order:
        in_order = True
        for i in range(1, index - 1):
            if not check_order(deepcopy(corrected[i]), deepcopy(corrected[i+1])):
                if i == 5:
                    pass
                in_order = False
                temp = deepcopy(corrected[i])
                corrected[i] = deepcopy(corrected[i+1])
                corrected[i+1] = deepcopy(temp)
    result = 1
    for i in corrected.keys():
        if corrected[i] == [[2]] or corrected[i] == [[6]]:
            result *= i
    return result    

with open("day13.txt" , "r") as f:
    data = f.read().split('\n\n')

print("Part One:", part_one(data))
data.append('[[2]]\n[[6]]')
print("Part Two:", part_two(data))
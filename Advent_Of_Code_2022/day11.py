import operator
from math import prod
ops = { "+": operator.add, "*": operator.mul }

def prep_monkeys(data_in):
    monkeys = {}
    current_monkey = 0
    for line in data_in:
        instruct = line[0]
        if instruct == 'Monkey':
            current_monkey = int(line[1].replace(':',''))
            monkeys[current_monkey] = {}
            monkeys[current_monkey]['count'] = 0
        elif instruct == 'Starting':
            monkeys[current_monkey]['items'] = [int(i.replace(',','')) for i in line[2:]]
        elif instruct == 'Operation:':
            monkeys[current_monkey]['op'] = line[3:]
        elif instruct == 'Test:':
            monkeys[current_monkey]['div_by'] = int(line[3])
        elif instruct == 'If':
            monkeys[current_monkey][line[1].replace(':','')] = int(line[5])
    return monkeys

def perform_op(item, operation):
    mky_op = operation[1]
    if operation[2] =='old':
        operand = item
    else:
        operand = int(operation[2])
    new = ops[mky_op](item,operand)
    return new

def monkeying_around(data_in, rounds, part):
    monkeys = prep_monkeys(data_in)
    monkey_list = sorted(monkeys.keys())
    # Multiply all the test modulos together to get a common multiple that won't screw with future modulo checks
    worry_fixer = prod([monkeys[mon]['div_by'] for mon in monkey_list])
    for i in range(rounds):
        for monkey in monkey_list:
            current_monkey = monkeys[monkey]
            for item in monkeys[monkey]['items']:
                operation = monkeys[monkey]['op']
                if part == 1:
                    new = perform_op(item,operation) // 3
                elif part == 2:
                    new = perform_op(item,operation) % worry_fixer
                test = new % current_monkey['div_by'] == 0
                monkeys[current_monkey[str(test).lower()]]['items'].append(new)
                current_monkey['count'] += 1
            current_monkey['items'] = []
    counts = sorted([monkeys[monkey]['count'] for monkey in monkeys.keys()], reverse=True)
    return counts[0] * counts[1]

            
            
with open("day11.txt" , "r") as f:
    data = [line.strip().split() for line in f.readlines() if line != '\n']

print("Part One:", monkeying_around(data,20,1))
print("Part Two:", monkeying_around(data,10000,2))


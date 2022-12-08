import re
from math import prod
from collections import defaultdict
field_name_search = re.compile('^[\w ]+(?=\:)')
valid_range_search = re.compile('\d+-\d+')
field_search = re.compile('\d+')
final_search = re.compile('departure')

def process_departures(col):
    dep = []
    for i in col.keys():
        if final_search.search(str(col[i])):
            dep.append(i)
    return dep

def field_process(valid, ticks):
    error_rate = 0
    columns = defaultdict(set)
    final_columns = {}
    for line in ticks:
        fields = field_search.findall(line)
        is_valid = True
        for i in range(0, len(fields)):
            field = int(fields[i])
            if field not in valid.keys():
                is_valid = False
                error_rate += field
        if is_valid:
            for i in range(0, len(fields)):
                field = int(fields[i])
                if len(columns[i]) == 0:
                    columns[i] = set(valid[field])
                else:
                    columns[i] = columns[i].intersection(set(valid[field]))
    target_size = len(columns)
    while len(final_columns) < target_size:
        for i in range(0, max(columns.keys()) + 1):
            if len(columns[i]) == 1:
                final_columns[i] = columns.pop(i)
            else:
                for final in final_columns.keys():
                    columns[i] = columns[i].difference(final_columns[final])
    return final_columns, error_rate

def build_validation_matrix(valid):
    out_dict = defaultdict(list)
    for line in valid:
        field_name = field_name_search.search(line)[0]
        ranges = valid_range_search.findall(line)
        for r in ranges:
            temp = tuple(map(int, r.split('-')))
            for i in range(temp[0], temp[1] + 1):
                out_dict[i].append(field_name)
    return out_dict

def start_process(valid, tick, other, part):
    valid_matrix = build_validation_matrix(valid)
    error_rate = 0
    col, error_rate = field_process(valid_matrix, other)
    dep_fields = process_departures(col)
    dep_prod = 1
    split_tick = list(map(int, tick[1].split(',')))
    for field in dep_fields:
        dep_prod = dep_prod * split_tick[field]
    if part == 1:
        return error_rate
    elif part == 2:
        return dep_prod

with open("input16.txt" , "r") as f:
	validation, my_ticket, other_tickets = [block.split('\n') for block in f.read().split("\n\n")]

print("Part One:", start_process(validation, my_ticket, other_tickets, part=1))
print("Part Two:", start_process(validation, my_ticket, other_tickets, part=2))
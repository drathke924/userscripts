from math import prod
# import time
# start_time = time.time()

def part_one(raw_time, raw_bus_list):
    leave_time = int(raw_time)
    bus_list = raw_bus_list.split(',')
    to_catch = 0
    wait_time = leave_time
    for bus in bus_list:
        if bus != 'x':
            check_wait = int(bus) - (leave_time % int(bus))
            if check_wait < wait_time:
                wait_time = check_wait
                to_catch = int(bus)
    return wait_time * to_catch

def part_two(raw_bus_list):
    bus_list = raw_bus_list.split(',')
    no_x = []
    offsets = {}
    for i in range(0, len(bus_list)):
        if bus_list[i] != 'x':
            offsets[int(bus_list[i])] = i
            no_x.append(int(bus_list[i]))
    maximum = prod(offsets.keys())
    leave_time = 0
    found_bus = [no_x[0]]
    found = False
    while not found:
        for bus in no_x:
            leave_time += prod(found_bus)
            if (leave_time + offsets[bus]) % bus == 0 and bus not in found_bus:
                found_bus.append(bus)
            if len(found_bus) == len(no_x):
                found = True
                break
    return leave_time % maximum

with open("input13.txt" , "r") as f:
	timestamp, busses = f.read().split("\n")

print("Part One: " + str(part_one(timestamp, busses)))
print("Part Two: " + str(part_two(busses)))
# print(time.time() - start_time)
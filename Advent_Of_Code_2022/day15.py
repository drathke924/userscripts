import re
import z3
digit_search = re.compile('\-?\d+')

def get_sensor_beacon(data_in):
    sensors = {}
    beacons = set()
    for line in data_in:
        s_x, s_y, b_x, b_y = list(map(int, digit_search.findall(line)))
        sensors[(s_x, s_y)] = abs(s_x - b_x) + abs(s_y - b_y)
        beacons.add((b_x, b_y))
    return sensors, beacons

def manhat(point_one, point_two):
    return abs(point_one[0] - point_two[0]) + abs(point_one[1] - point_two[1])

def find_edge(sensors, pos, dir):
    x, row = pos
    closer = []
    for sensor in sensors.keys():
        if manhat(pos, sensor) <= sensors[sensor]:
            closer.append(sensor)
    if dir > 0:
        edgiest = [sensor for sensor in sensors.keys() if sensor[0] == max([x for x, y in closer])][0]
    elif dir < 0:
        edgiest = [sensor for sensor in sensors.keys() if sensor[0] == min([x for x, y in closer])][0]
    if dir > 0:
        if pos[0] > edgiest[0] and max([sensors[point] - manhat(pos, point) for point in closer]) == 0:
            return x
        elif len(closer) > 1 or manhat(pos, edgiest) < sensors[edgiest]:
            new_x = x + max([1, (sensors[edgiest] - manhat(pos, edgiest))]) * dir
            return find_edge(sensors, (new_x, row), dir)
    elif dir < 0:
        if pos[0] < edgiest[0] and max([sensors[point] - manhat(pos, point) for point in closer]) == 0:
            return x
        elif len(closer) > 1 or manhat(pos, edgiest) < sensors[edgiest]:
            new_x = x + max([1, (sensors[edgiest] - manhat(pos, edgiest))]) * dir
            return find_edge(sensors, (new_x, row), dir)
    else:
        raise Exception("This shouldn't be happening. We've gone too far!")


def no_beacon_row(sensors, beacons, row):
    start_x = int(sum([y for x,y in sensors.keys()])/len(sensors.keys()))
    beacons_on_row = len([beacon for beacon in beacons if beacon[1] == row])
    # print(start_x)
    # print(beacons_on_row)
    # print(find_edge(sensors, (start_x, row), 1), find_edge(sensors, (start_x, row), -1))
    return find_edge(sensors, (start_x, row), 1) - find_edge(sensors, (start_x, row), -1) - beacons_on_row + 1

# airlifted and modified to fit from u/hugh_tc https://www.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0af5cy/
def part_two(data_in):
    s = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    s.add(0 <= x)
    s.add(x <= 4000000)
    s.add(0 <= y)
    s.add(y <= 4000000)
    def z3_abs(x):
        return z3.If(x >= 0, x, -x)
    for line in data:
        sx, sy, bx, by = [int(x) for x in digit_search.findall(line)]
        m = abs(sx - bx) + abs(sy - by)
        s.add(z3_abs(sx - x) + z3_abs(sy - y) > m)
    s.check()
    outx, outy = s.model()[x].as_long(), s.model()[y].as_long()
    return outx * 4000000 + outy

with open("day15.txt" , "r") as f:
    data = f.read().split('\n')

sensor_list, beacon_list = get_sensor_beacon(data)
print("Part One:", no_beacon_row(sensor_list, beacon_list, 2000000))
print("Part Two:", part_two(data))


from collections import deque

def create_graph(map_in, x_size, y_size):
    heightgraph = {}
    for y in range(0, y_size):
        for x in range(0, x_size):
            heightgraph[(x,y)] = []
            curr = map_in[(x,y)]
            neighbors = [(x-1,y), (x,y-1), (x+1,y), (x,y+1)]
            for neighbor in neighbors:
                if neighbor in map_in.keys() and map_in[neighbor] <= curr + 1:
                    heightgraph[(x,y)].append(neighbor)
    return heightgraph

def create_map(data_in):
    heightmap = {}
    part_two = []
    for y in range(0, len(data_in)):
        for x in range(0, len(data_in[y])):
            curr = data_in[y][x]
            if curr == 'S':
                start_point = (x, y)
                heightmap[(x,y)] = 0
            elif curr == 'E':
                end_point = (x, y)
                heightmap[(x,y)] = 27
            elif curr == 'a':
                heightmap[(x,y)] = 1
                part_two.append((x,y))
            else:
                heightmap[(x,y)] = ord(curr) - 96
    return heightmap, start_point, end_point, part_two

def find_path(graph, start, end):
    dist = {start: [start]}
    q = deque()
    q.append(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    weird = dist.get(end)
    out = []
    if weird:
        while len(weird) > 1:
            out.insert(0,weird.pop(1))
            weird = weird[0]
    return out

def part_two(graph, start, end, part_two):
    shortest = find_path(graph, start, end)
    for newstart in part_two:
        newpath = find_path(graph, newstart, end)
        if 1 < len(newpath) < len(shortest):
            shortest = newpath
    return shortest


def prep_data(data_in):
    x_size, y_size = len(data_in[0]), len(data_in)
    heightmap, start_point, end_point, part_two = create_map(data_in)
    heightgraph = create_graph(heightmap, x_size, y_size)
    return heightmap, heightgraph, x_size, y_size, start_point, end_point, part_two

with open("day12.txt" , "r") as f:
    data, graph, width, height, start, end, parttwo = prep_data(f.read().split('\n'))

print("Part One:", len(find_path(graph, start, end)))
print("Part Two:", len(part_two(graph, start, end, parttwo)))
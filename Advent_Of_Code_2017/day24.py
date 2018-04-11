from operator import itemgetter

with open("day24.txt", "r") as f:
    DATA = list(map(lambda x: tuple(map(int, x.split("/"))), f.read().splitlines()))

nodes = {}
for node in DATA:
    if node[0] not in nodes.keys():
        nodes[node[0]] = set()
    nodes[node[0]].add(node[1])
    if node[1] not in nodes.keys():
        nodes[node[1]] = set()
    nodes[node[1]].add(node[0])

start = (0, 0)
all_bridges = set()

def bridge_generator(current, bridge, node_set):
    for i in node_set[current[1]]:
        if (current[1], i) not in bridge and (i, current[1]) not in bridge:
            yield set(list(bridge) + [(current[1], i)])
            yield from bridge_generator((current[1], i), set(list(bridge) + [(current[1], i)]), node_set)

sums = []
lengths = []

for bridge in bridge_generator(start, set(), nodes):
    strength = sum(list(map(sum, bridge)))
    lengths.append(len(bridge))
    sums.append(strength)

print(max(sums))
print(sorted(list(zip(lengths, sums)), key=itemgetter(0, 1))[-1])

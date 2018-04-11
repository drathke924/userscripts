with open("day24test.txt", "r") as f:
    DATA = list(map(lambda x: tuple(map(int, x.split("/"))), f.read().splitlines()))

print(DATA)

def does_connect(node_one, node_two, port):
    if node_one[port] in node_two:
        return True

def make_bridge(search_set):

def is_touching(h, t):
    if t[0] in range(h[0]-1, h[0]+2) and t[1] in range(h[1]-1, h[1]+2):
        return True
    return False

def move_head(direction,h):
    if direction == 'U':
        return (h[0],h[1]+1)
    elif direction == 'R':
        return (h[0]+1,h[1])
    elif direction == 'D':
        return (h[0],h[1]-1)
    elif direction == 'L':
        return(h[0]-1,h[1])
    else:
        raise ValueError('Direction not valid')

def move_tail(h,t):
    to_move = [t[0], t[1]]
    if h[0] > t[0]:
        to_move[0] += 1
    elif h[0] < t[0]:
        to_move[0] -= 1
    if h[1] > t[1]:
        to_move[1] += 1
    elif h[1] < t[1]:
        to_move[1] -= 1
    return tuple(to_move)

def do_da_snake(data_in, size):
    rope_pos = [(0,0) for i in range(size)]
    visited = set()
    visited.add((0,0))
    for dir, steps_raw in data_in:
        steps = int(steps_raw)
        for i in range(0, steps):
            rope_pos[0] = move_head(dir, rope_pos[0])
            for a in range(len(rope_pos) - 1):
                b = a + 1
                if not is_touching(rope_pos[a], rope_pos[b]):
                    rope_pos[b] = move_tail(rope_pos[a], rope_pos[b])
            visited.add(rope_pos[-1])
    return len(visited)

with open("day9.txt" , "r") as f:
    data = [line.strip().split() for line in f.readlines()]


print("Part One:", do_da_snake(data, 2))
print("Part Two:", do_da_snake(data, 10))
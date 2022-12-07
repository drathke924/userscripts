def build_struct(data_in):
    current_dir = "/"
    dirs = {'/':0}
    for line in data_in:
        instruct = line.split()
        if instruct[1] == 'cd':
            current_dir = change_dir(current_dir, instruct[2])
        elif instruct[1] == 'ls':
            pass
        else:
            if not instruct[0] == 'dir':
                file_size = int(instruct[0])
                if current_dir != '/':
                    temp_struct = current_dir.split('/')
                    for i in range(2, len(temp_struct)):
                        dir = '/'.join(temp_struct[0:i])
                        dirs[dir] += file_size
                    dirs['/'] += file_size
                dirs[current_dir] += file_size
            elif current_dir == '/':
                dirs[current_dir + instruct[1]] = 0
            else:
                dirs[current_dir + '/' + instruct[1]] = 0
    return dirs

def change_dir(current_dir, new_dir):
    if new_dir =='/':
        current_dir = '/'
    elif new_dir == '..':
        temp_struct = current_dir.split('/')
        temp_struct.pop()
        current_dir = '/'.join(temp_struct)
    elif current_dir == '/':
        current_dir = current_dir + new_dir
    else:
        current_dir = current_dir + '/' + new_dir
    return current_dir

def part_one(dirs):
    size = 0
    for dir in dirs.keys():
        if dirs[dir] <= 100000:
            size += dirs[dir]
    return size

def part_two(dirs):
    drive_size = 70000000
    needed_space = 30000000
    unused_space = drive_size - dirs['/']
    need_to_delete = needed_space - unused_space
    size = drive_size
    for dir in dirs.keys():
        if need_to_delete <= dirs[dir] < size:
            size = dirs[dir]
    return size

with open("day7.txt" , "r") as f:
    data = f.read().split('\n')

built_dirs = build_struct(data)
print("Part One: " + str(part_one(built_dirs)))
print("Part Two: " + str(part_two(built_dirs)))
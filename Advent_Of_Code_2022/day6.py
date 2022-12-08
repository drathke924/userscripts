def find_marker(data_in, size):
    buffer = list(data_in[0:size])
    buffer.reverse()
    for i in range(size, len(data_in)):
        if len(set(buffer)) == size:
            return i
        else:
            buffer.pop()
            buffer.insert(0, data_in[i])

with open("day6.txt" , "r") as f:
    data = f.read()

print("Part One: " + str(find_marker(data, 4)))
print("Part Two: " + str(find_marker(data, 14)))
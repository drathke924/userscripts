import re

def newline_split(data_in):
    return data_in.split("\n")

def part_one(board_in, instruct_in):
    board_state = build_board_state(board_in)
    for current_instruct in instruct_in:
        cycles, stack_from, stack_to = list(map(int, re.findall("\d+", current_instruct)))
        for i in range(0, cycles):
            board_state[stack_to - 1].append(board_state[stack_from - 1].pop())
    return "".join([board_state[x][-1] for x in range(0, 9)])

def part_two(board_in, instruct_in):
    board_state = build_board_state(board_in)
    for current_instruct in instruct_in:
        num_crates, stack_from, stack_to = list(map(int, re.findall("\d+", current_instruct)))
        held_crates = []
        for i in range(0, num_crates):
            held_crates.insert(0, board_state[stack_from - 1].pop())
        board_state[stack_to - 1].extend(held_crates)
    return "".join([board_state[x][-1] for x in range(0, 9)])

def build_board_state(board_in):
    board_state = {i:[] for i in range(0,9)}
    for line in board_in:
        for i in range(0, 9):
            top_of_stack = line[i*4+1]
            if top_of_stack != " " and not top_of_stack.isdigit():
                board_state[i].insert(0, top_of_stack)
    return board_state

with open("day5.txt" , "r") as f:
    board, instructions = list(map(newline_split, f.read().split("\n\n")))



print("Part One: " + part_one(board, instructions))
print("Part Two: " + part_two(board, instructions))
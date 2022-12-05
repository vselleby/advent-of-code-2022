#         [H]         [S]         [D]
#     [S] [C]         [C]     [Q] [L]
#     [C] [R] [Z]     [R]     [H] [Z]
#     [G] [N] [H] [S] [B]     [R] [F]
# [D] [T] [Q] [F] [Q] [Z]     [Z] [N]
# [Z] [W] [F] [N] [F] [W] [J] [V] [G]
# [T] [R] [B] [C] [L] [P] [F] [L] [H]
# [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
#  1   2   3   4   5   6   7   8   9
stack_one = ['H', 'T', 'Z', 'D']
stack_two = ['Q', 'R', 'W', 'T', 'G', 'C', 'S']
stack_three = ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H']
stack_four = ['L', 'C', 'N', 'F', 'H', 'Z']
stack_five = ['G', 'L', 'F', 'Q', 'S']
stack_six = ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S']
stack_seven = ['Z', 'F', 'J']
stack_eight = ['D', 'L', 'V', 'Z', 'R', 'H', 'Q']
stack_nine = ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']
stacks = [stack_one, stack_two, stack_three, stack_four, stack_five, stack_six, stack_seven, stack_eight, stack_nine]


def solve_a(content):
    for line in content:
        split_line = line.strip().split(' ')
        stacks_to_move = int(split_line[1])
        from_stack = stacks.__getitem__(int(split_line[3]) - 1)
        to_stack = stacks.__getitem__(int(split_line[5]) - 1)
        for i in range(stacks_to_move):
            to_stack.append(from_stack.pop())
    result = ""
    for i in range(len(stacks)):
        result += stacks.__getitem__(i)[-1]
    return result


def solve_b(content):
    for line in content:
        split_line = line.strip().split(' ')
        stacks_to_move = int(split_line[1])
        from_stack = stacks.__getitem__(int(split_line[3]) - 1)
        to_stack = stacks.__getitem__(int(split_line[5]) - 1)
        move_buffer = []
        for i in range(stacks_to_move):
            move_buffer.insert(0, from_stack.pop())
        to_stack.extend(move_buffer)
    result = ""
    for i in range(len(stacks)):
        result += stacks.__getitem__(i)[-1]
    return result


if __name__ == '__main__':
    with open("input/input5.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))

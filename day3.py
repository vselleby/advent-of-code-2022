def split_in_half(string):
    string = str.strip(string)
    first_half = string[0:len(string) // 2]
    second_half = string[len(string) // 2:]
    return [first_half, second_half]


def calculate_priority(match_string):
    if match_string.isupper():
        offset = 64 - 26
    else:
        offset = 96
    return [ord(char) for char in match_string][0] - offset


def solve_a(content):
    priority_sum = 0
    for line in content:
        [first, second] = split_in_half(line)
        matches = set(first).intersection(second)
        assert len(matches) == 1
        priority_sum = priority_sum + calculate_priority(matches.pop())
    return priority_sum


def solve_b(content):
    priority_sum = 0
    group = []
    for line in content:
        group.append(str.strip(line))
        if len(group) == 3:
            matches = set(group[0]).intersection(group[1]).intersection(group[2])
            assert len(matches) == 1
            priority_sum = priority_sum + calculate_priority(matches.pop())
            group = []
    return priority_sum


if __name__ == '__main__':
    with open("input/input3.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))

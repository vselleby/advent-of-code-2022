import pandas as pd


def is_pair_fully_contained(pair):
    first_range = pair[0].split("-")
    second_range = pair[1].split("-")
    if int(first_range[0]) <= int(second_range[0]) and int(first_range[1]) >= int(second_range[1]):
        return True
    elif int(first_range[0]) >= int(second_range[0]) and int(first_range[1]) <= int(second_range[1]):
        return True
    else:
        return False


def is_pair_overlap(pair):
    first_range = pair[0].split("-")
    first_interval = pd.Interval(int(first_range[0]), int(first_range[1]), closed='both')
    second_range = pair[1].split("-")
    second_interval = pd.Interval(int(second_range[0]), int(second_range[1]), closed='both')
    return first_interval.overlaps(second_interval)


def solve_a(content):
    no_contained = 0
    for line in content:
        pair = line.strip().split(",")
        if is_pair_fully_contained(pair):
            no_contained += 1
    return no_contained


def solve_b(content):
    no_overlap = 0
    for line in content:
        pair = line.strip().split(",")
        if is_pair_overlap(pair):
            no_overlap += 1
    return no_overlap


if __name__ == '__main__':
    with open("input/input4.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))

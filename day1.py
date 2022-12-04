def solve_a(content):
    maximum_calories = 0
    current_calories = 0
    for line in content:
        stripped = str.strip(line)
        if stripped == "":
            if current_calories > maximum_calories:
                maximum_calories = current_calories
            current_calories = 0
        else:
            current_calories = current_calories + int(stripped)
    return maximum_calories


def solve_b(content):
    maximum_calories = [0]
    current_calories = 0
    for line in content:
        stripped = str.strip(line)
        if stripped == "":
            if current_calories > min(maximum_calories):
                if len(maximum_calories) == 3:
                    maximum_calories.remove(min(maximum_calories))
                maximum_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories = current_calories + int(stripped)
    return sum(maximum_calories)


if __name__ == '__main__':
    with open("input/input1.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))

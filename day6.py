def solve_a(content):
    content = content.replace("\n", "")
    last_characters = []
    index = 0
    for char in content:
        index += 1
        if len(last_characters) == 4:
            last_characters.pop(0)
        last_characters.append(char)
        if len(set(last_characters)) == 4:
            return index


def solve_b(content):
    content = content.replace("\n", "")
    last_characters = []
    index = 0
    for char in content:
        index += 1
        if len(last_characters) == 14:
            last_characters.pop(0)
        last_characters.append(char)
        if len(set(last_characters)) == 14:
            return index


if __name__ == '__main__':
    with open("input/input6.txt") as file:
        file_content = file.read()
        print(solve_b(file_content))

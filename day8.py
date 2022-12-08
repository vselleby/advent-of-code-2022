def tree_visible_left(forest, row, col):
    temp_col = col
    while temp_col > 0:
        temp_col -= 1
        if forest[row][temp_col] >= forest[row][col]:
            return False
    return True


def tree_visible_top(forest, row, col):
    temp_row = row
    while temp_row > 0:
        temp_row -= 1
        if forest[temp_row][col] >= forest[row][col]:
            return False
    return True


def tree_visible_right(forest, row, col):
    temp_col = col
    while temp_col < 98:
        temp_col += 1
        if forest[row][temp_col] >= forest[row][col]:
            return False
    return True


def tree_visible_bottom(forest, row, col):
    temp_row = row
    while temp_row < 98:
        temp_row += 1
        if forest[temp_row][col] >= forest[row][col]:
            return False
    return True


def tree_visible(forest, row, col):
    return tree_visible_left(forest, row, col) or tree_visible_top(forest, row, col) or \
           tree_visible_right(forest, row, col) or tree_visible_bottom(forest, row, col)


def solve_a(content):
    visible_trees = 0
    forest = load_data(content)
    for row in range(99):
        for col in range(99):
            if tree_visible(forest, row, col):
                visible_trees += 1
    return visible_trees


def trees_visible_left(forest, row, col):
    trees_visible = 0
    temp_col = col
    while temp_col > 0:
        temp_col -= 1
        if forest[row][temp_col] >= forest[row][col]:
            return trees_visible + 1
        else:
            trees_visible += 1
    return trees_visible


def trees_visible_top(forest, row, col):
    trees_visible = 0
    temp_row = row
    while temp_row > 0:
        temp_row -= 1
        if forest[temp_row][col] >= forest[row][col]:
            return trees_visible + 1
        else:
            trees_visible += 1
    return trees_visible


def trees_visible_right(forest, row, col):
    trees_visible = 0
    temp_col = col
    while temp_col < 98:
        temp_col += 1
        if forest[row][temp_col] >= forest[row][col]:
            return trees_visible + 1
        else:
            trees_visible += 1
    return trees_visible


def trees_visible_bottom(forest, row, col):
    trees_visible = 0
    temp_row = row
    while temp_row < 98:
        temp_row += 1
        if forest[temp_row][col] >= forest[row][col]:
            return trees_visible + 1
        else:
            trees_visible += 1
    return trees_visible


def other_trees_visible(forest, row, col):
    return trees_visible_left(forest, row, col) * trees_visible_top(forest, row, col) * \
           trees_visible_right(forest, row, col) * trees_visible_bottom(forest, row, col)


def solve_b(content):
    best_view = 0
    forest = load_data(content)
    for row in range(99):
        for col in range(99):
            if other_trees_visible(forest, row, col) > best_view:
                best_view = other_trees_visible(forest, row, col)
    return best_view


def load_data(content):
    forest = []
    row = 0
    for line in content:
        forest.append([])
        for number in line.strip():
            forest[row].append(int(number))
        row += 1
    return forest


if __name__ == '__main__':
    with open("input/input8.txt") as file:
        file_content = file.readlines()
        print(solve_a(file_content))
        print(solve_b(file_content))

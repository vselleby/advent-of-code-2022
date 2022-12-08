class Directory:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

    def cd(self, path):
        if path == "/":
            return self
        elif path == "..":
            return self.parent
        else:
            return [child for child in self.children if child.name == path][0]

    def mkdir(self, path):
        self.children.append(Directory(path, self, 0))

    def touch(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.touch(size)

    def get_all_children(self):
        yield self
        for child in self.children:
            yield from child.get_all_children()


def load_file_system(content):
    root = Directory("/", None, 0)
    current_dir = root
    for cmd in content:
        if cmd.startswith("$ cd"):
            dir_name = cmd.split()[2]
            current_dir = current_dir.cd(dir_name)
        elif cmd.startswith("$ ls"):
            None
        elif cmd.startswith("dir"):
            dir_name = cmd.split()[1]
            current_dir.mkdir(dir_name)
        else:
            file_size = int(cmd.split()[0])
            current_dir.touch(file_size)
    return root


def solve_a(content):
    root = load_file_system(content)
    total_size = 0
    for directory in root.get_all_children():
        if directory.size < 100000:
            total_size += directory.size
    return total_size


def solve_b(content):
    root = load_file_system(content)
    total_disk = 70000000
    update_disk = 30000000
    free_disk = total_disk - root.size
    required_space = update_disk - free_disk
    min_candidate = total_disk

    for directory in root.get_all_children():
        if required_space < directory.size < min_candidate:
            min_candidate = directory.size
    return min_candidate


if __name__ == '__main__':
    with open("input/input7.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))

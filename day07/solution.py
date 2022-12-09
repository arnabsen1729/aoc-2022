
PART1_RES = 95437
PART2_RES = 24933642

class Node:
    def __init__(self, name: str, isDirectory: bool, size: int = 0) -> None:
        self.name = name
        self.isDirectory = isDirectory
        self.size = size
        self.children = []

        if not self.isDirectory:
            assert self.children == []

    def add_child(self, child: 'Node') -> None:
        assert self.isDirectory
        self.children.append(child)

    def get_size(self) -> int:
        if self.isDirectory:
            return sum([child.get_size() for child in self.children])
        else:
            return self.size

    def __str__(self) -> str:
        return f'Node({self.name}, {self.isDirectory}, {self.size}, {self.children})'

    def tree(self, padding: str = '') -> str:
        if self.isDirectory:
            print(f'{padding}- {self.name} (dir)')
            for child in self.children:
                child.tree(padding + '  ')
        else:
            print(f'{padding}- {self.name} (file, size={self.size})')


def parse_input(f):
    lines = f.readlines()
    root = Node('/', True, 0)
    current_path = [root]
    for line in lines[1:]:
        if line.startswith('$ cd '):
            dir_name = line[5:].strip()
            if dir_name == '..':
                current_path.pop()
            else:
                # find the dir in current_path
                dir_exists = False
                for child in current_path[-1].children:
                    if child.name == dir_name:
                        current_path.append(child)
                        dir_exists = True
                        break
                assert dir_exists
        elif line.startswith('$ ls'):
            pass
        else:
            # output of ls
            if line.startswith('dir'):
                dir_name = line[4:].strip()
                dir = Node(dir_name, True, 0)
                current_path[-1].add_child(dir)
            else:
                file_size, file_name = line.split()
                file = Node(file_name, False, int(file_size))
                current_path[-1].add_child(file)

    # root.tree()
    return root

def get_dir_sizes(root: Node) -> list:
    if root.isDirectory:
        dir_size = root.get_size()
        return [dir_size] + sum([get_dir_sizes(child) for child in root.children], [])
    else:
        return []

def part1(root):
    LIMIT = 100000
    dir_sizes = sum([s if s <= LIMIT else 0 for s in get_dir_sizes(root)])

    return dir_sizes


def part2(root):
    TOTAL_AVAILABLE_DISK_SPACE = 70000000
    MIN_UNUSED_SPACE = 30000000
    
    dir_sizes = sorted(get_dir_sizes(root))
    root_size = dir_sizes[-1]
    for s in dir_sizes:
        size_left = TOTAL_AVAILABLE_DISK_SPACE - root_size + s
        if size_left >= MIN_UNUSED_SPACE:
            return s
    
    raise Exception('No solution found')


def main():
    global f
    f = open('test.txt')
    root = parse_input(f)
    assert part1(root) == PART1_RES
    assert part2(root) == PART2_RES
    f.close()

    f = open('input.txt')
    root = parse_input(f)
    print('Part 1:', part1(root))
    print('Part 2:', part2(root))
    f.close()


if __name__ == '__main__':
    main()

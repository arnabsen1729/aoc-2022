import copy

f = open('test.txt') 
f = open('input.txt')

lines = f.read()

class CrateStack:
    def __init__(self, len) -> None:
        self.stack = [[] for _ in range(len)]
        self.len = len

    def insert(self, index, value):
        self.stack[index].append(value)

    def display(self):
        for i in range(self.len):
            print(f'{i+1}: {self.stack[i]}')

    def move(self, count, from_index, to_index):
        from_index -= 1
        to_index -= 1
        for _ in range(count):
            self.stack[to_index].append(self.stack[from_index].pop())

    def move_together(self, count, from_index, to_index):
        from_index -= 1
        to_index -= 1
        self.stack[to_index].extend(self.stack[from_index][-count:])
        self.stack[from_index] = self.stack[from_index][:-count]


    def get_top(self,):
        return ''.join([self.stack[i][-1] if len(self.stack[i]) > 0 else '' for i in range(self.len)])

class Command:
    def __init__(self, crates, source, dest) -> None:
        self.crates = crates
        self.source = source
        self.dest = dest

    def display(self):
        print(f'move {self.crates} from {self.source} to {self.dest}')

def parse(lines):
    orientation, commands = lines.split('\n\n')

    numbering = orientation.split('\n')[-1]
    len = int(numbering.split()[-1])
    crates = CrateStack(len)

    orientation = orientation.split('\n')[:-1]

    for stack in orientation[::-1]:
        for i in range(len):
            pos = i*4 + 1
            if stack[pos] != ' ':
                crates.insert(i, stack[pos])

    commands = commands.split('\n')
    commands = [command.split() for command in commands]
    commands = [Command(int(command[1]), int(command[3]), int(command[5])) for command in commands]

    return crates, commands

crates, commands = parse(lines)
crates_2 = copy.deepcopy(crates)

for c in commands:
    crates.move(c.crates, c.source, c.dest)

print('Part 1:', crates.get_top())

for c in commands:
    crates_2.move_together(c.crates, c.source, c.dest)

print('Part 2:', crates_2.get_top())
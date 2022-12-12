from typing import Callable

ANSWER = 2713310158
MOD = 1

class Monkey:
    def __init__(self, id: int, starting_items: list[int], operation: Callable[[int], int],
                 test: Callable[[int], int]):
        self.id = id
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspection_count = 0

    def __str__(self) -> str:
        return f'''Monkey {self.id}:
        Starting items: {self.items}
        Operation: {self.operation}
        Test: {self.test}'''

    def get_item(self):
        return self.items.pop(0)

    def print_items(self):
        print(f'Monkey {self.id}: {self.items}')


def parse_monkey(data: str) -> Monkey:
    global MOD
    lines = data.splitlines()
    id = int(lines[0].split()[1][:-1])
    starting_items = list(map(int, lines[1].replace('Starting items:', '').strip().split(', ')))
    op_data = lines[2].replace('Operation: new = old', '').strip().split()
    operation = None
    if op_data[0] == '*':
        if op_data[1] == 'old':
            operation = lambda x: x * x
        else:
            value = int(op_data[1])
            operation = lambda x: x * value
    elif op_data[0] == '+':
        if op_data[1] == 'old':
            operation = lambda x: x + x
        else:
            value = int(op_data[1])
            operation = lambda x: x + value


    divisor = int(lines[3].split()[-1])
    MOD *= divisor
    if_true_id =  int(lines[4].split()[-1])
    if_false_id =  int(lines[5].split()[-1])
    test = lambda x: if_true_id if x % divisor == 0 else if_false_id
    return Monkey(id, starting_items, operation, test)


def parse(file):
    data = file.read()
    return [parse_monkey(monkey) for monkey in data.split('\n\n')]


def solve(monkeys: list[Monkey]):
    global MOD
    ROUNDS = 10000
    for x in range(ROUNDS):
        for index in range(len(monkeys)):
            monkey = monkeys[index]
            for _ in range(len(monkey.items)):
                item = monkey.get_item()
                monkey.inspection_count += 1
                new_item = monkey.operation(item)%MOD
                monkeys[monkey.test(new_item)].items.append(new_item)
        
    counts = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
    return counts[0]*counts[1]

def main():
    global f
    global MOD
    f = open('test.txt')
    data = parse(f)
    assert solve(data) == ANSWER
    f.close()
    MOD = 1
    f = open('input.txt')
    data = parse(f)
    print('Part 2:', solve(data))
    f.close()


if __name__ == '__main__':
    main()


PART1_RES = 13
PART2_RES = 36

import math

def get_eucledian_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, other: 'Coord') -> None:
        self.x += other.x
        self.y += other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Rope:
    dir_vectors = {
        'U': Coord(0, 1),
        'D': Coord(0, -1),
        'L': Coord(-1, 0),
        'R': Coord(1, 0),
    }
    def __init__(self, length = 1):
        self.head = Coord(0, 0)
        self.tail = Coord(0, 0)
        self.length = length
    
    def move(self, direction,):
        vector = self.dir_vectors[direction]
        self.head.shift(vector)

        dist = get_eucledian_distance(self.head.x, self.head.y, self.tail.x, self.tail.y)
        if dist <= self.length*math.sqrt(2):
            # it is touching
            return

        x_gap = sign(self.head.x - self.tail.x)
        y_gap = sign(self.head.y - self.tail.y)

        self.tail.shift(Coord(x_gap, y_gap))

def parse(lines):
    return [[line.split()[0], int(line.split()[1])] for line in lines]


def part1(cmds) -> int:
    position = set()
    rope = Rope()
    for cmd in cmds:
        for _ in range(cmd[1]):
            rope.move(cmd[0])
            position.add((rope.tail.x, rope.tail.y))

    return len(position)

def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    cmds = parse(lines)
    # assert part1(cmds) == PART1_RES
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    cmds = parse(lines)
    print('Part 1:', part1(cmds))
    f.close()

if __name__ == '__main__':
    main()

'''

#H###
x####
'''
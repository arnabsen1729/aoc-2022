
PART1_RES = 13
PART2_RES = 36

import os
import time

import math

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_eucledian_distance(x1: int, y1: int, x2:int, y2:int) -> float:
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
    def __init__(self, length = 2):
        self.body = [Coord(0, 0) for _ in range(length)]
        self.length = length

    def move_head(self, direction):
        vector = self.dir_vectors[direction]
        self.body[0].shift(vector)

        def follow(index):
            prev = self.body[index - 1]
            curr = self.body[index]
            dist = get_eucledian_distance(prev.x, prev.y, curr.x, curr.y)
            if dist <= math.sqrt(2):
                return

            x_gap = sign(prev.x - curr.x)
            y_gap = sign(prev.y - curr.y)

            self.body[index].shift(Coord(x_gap, y_gap))
    
        for body_index in range(1, self.length):
            follow(body_index)

    def get_tail(self):
        return self.body[-1]

    def display(self):
        cls()
        LENGTH = 40
        WIDTH = 50
        SHIFT_X = 13
        SHIFT_Y = 13
        matrix = [['.'] * WIDTH for _ in range(LENGTH)]
        for index, coord in enumerate(self.body):
            if matrix[coord.x + SHIFT_X][coord.y + SHIFT_Y] == '.':
                matrix[coord.x + SHIFT_X][coord.y + SHIFT_Y] = str(index)

        for row in matrix:
            print(''.join(row))
        # input()
        time.sleep(0.1)
        

def parse(lines):
    return [[line.split()[0], int(line.split()[1])] for line in lines]

def part2(cmds) -> int:
    position = set()
    rope = Rope(10)
    position.add((0, 0))
    for cmd in cmds:
        for _ in range(cmd[1]):
            rope.move_head(cmd[0])
            tail = rope.get_tail()
            position.add((tail.x, tail.y))
            # rope.display()

    return len(position)

def main():
    global f

    f = open('input.txt')
    lines = f.readlines()
    cmds = parse(lines)
    print('Part 2:', part2(cmds))
    f.close()

if __name__ == '__main__':
    main()

'''

#H###
x####
'''
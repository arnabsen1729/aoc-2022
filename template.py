
PART1_RES = 0
PART2_RES = 0

def part1(f):
    lines = f.readlines()
    return 0

def part2(f):
    lines = f.readlines()
    return 0

def main():
    global f
    f = open('test.txt')
    assert part1(f) == PART1_RES
    assert part2(f) == PART2_RES
    f.close()

    f = open('input.txt')
    print('Part 1:', part1(f))
    print('Part 2:', part2(f))
    f.close()

    
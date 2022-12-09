
PART1_RES = 0
PART2_RES = 0

def part1(lines):
    return 0

def part2(lines):
    return 0

def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    assert part1(lines) == PART1_RES
    assert part2(lines) == PART2_RES
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))
    f.close()

if __name__ == '__main__':
    main()
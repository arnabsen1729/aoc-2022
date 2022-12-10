ANSWER = 0

def parse(lines):
    return lines

def part1(data):
    return 0

def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    data = parse(lines)
    assert part1(data) == ANSWER
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    data = parse(lines)
    print('Part 1:', part1(data))
    f.close()

if __name__ == '__main__':
    main()
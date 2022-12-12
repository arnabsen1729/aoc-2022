ANSWER = 0

def parse(lines):
    return lines

def solve(data):
    return 0

def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    data = parse(lines)
    res = solve(data)
    print('Test :', res)
    assert res == ANSWER
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    data = parse(lines)
    print('Final :', solve(data))
    f.close()

if __name__ == '__main__':
    main()

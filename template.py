ANSWER = 0

def parse(f):
    return ''

def solve(data):
    return 0

def main():
    global f
    f = open('test.txt')
    data = parse(f)
    res = solve(data)
    print('Test :', res)
    assert res == ANSWER
    f.close()

    f = open('input.txt')
    data = parse(f)
    print('Final :', solve(data))
    f.close()

if __name__ == '__main__':
    main()

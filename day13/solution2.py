ANSWER = 140


def split(line: str) -> list[str | int]:
    res = []
    item = ''
    for c in line:
        if c == '[' or c == ']':
            if item != '':
                res.append(int(item))
                item = ''
            res.append(c)
        elif c == ',':
            if item != '':
                res.append(int(item))
            item = ''
        else:
            item += c
    return res

def parse_list_helper(arr: list[str | int], index = 0) -> tuple[list[int] | None, int]:
    if len(arr) == 0:
        return (None, index)

    res = []
    i = index
    while i < len(arr):
        if arr[i] == '[':
            sub_list, end = parse_list_helper(arr, i + 1)
            res.append(sub_list)
            i = end
        elif arr[i] == ']':
            return (res, i)
        else:
            res.append(arr[i])

        i += 1
    
    return (res[0], i)



def parse_list(list: str):
    return parse_list_helper(split(list), 0)[0]
    # [1,[2,[3,[4,[5,6,7]]]],8,9]
    

def parse(lines):
    pairs = [pair.split('\n') for pair in lines.split('\n\n')]
    final_pairs = []

    for p in pairs:
        final_pairs.append(parse_list(p[0]))
        final_pairs.append(parse_list(p[1]))

    return final_pairs

def compare(a, b):
    for i, j in zip(a, b):
        if type(i) == int and type(j) == int:
            if i < j:
                return 1
            elif i > j:
                return -1
        elif type(i) == list and type(j) == list:
            res = compare(i, j)
            if res != 0:
                return res
        elif type(i) == int and type(j) == list:
            res = compare([i], j)
            if res != 0:
                return res
        elif type(i) == list and type(j) == int:
            res = compare(i, [j])
            if res != 0:
                return res

    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        return 0

def bubble_sort(arr):
    for i in range(len(arr)):
        c = 0
        for j in range(len(arr) - 1):
            if compare(arr[j], arr[j + 1]) != 1:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                c += 1
        if c == 0:
            break
    
    return arr

def solve(pairs):
    pairs.append([[2]])
    pairs.append([[6]])
    pairs = bubble_sort(pairs)
    res = (pairs.index([[2]])+1)*(pairs.index([[6]])+1)
    return res




def main():
    global f
    f = open('test.txt')
    lines = f.read()
    data = parse(lines)
    res = solve(data)
    print('Test :', res)
    assert res == ANSWER
    f.close()

    f = open('input.txt')
    lines = f.read()
    data = parse(lines)
    print('Final :', solve(data))
    f.close()


if __name__ == '__main__':
    main()

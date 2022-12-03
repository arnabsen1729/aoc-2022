f = open('test.txt') 
f = open('input.txt')

lines = f.readlines()

def get_common_letters(strs):
    s1 = set(strs[0])
    for i in range(1, len(strs)):
        s1 = s1.intersection(strs[i])
    return list(s1)

def get_priority(char):
    if ord(char) >= ord('a'):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

def part_1():
    count = 0
    for line in lines:
        rucksack = line.strip()
        l = len(rucksack)
        common_letters = get_common_letters([rucksack[:l//2], rucksack[l//2:]])
        if len(common_letters) == 0:
            continue
        count += get_priority(common_letters[0])
    return count

print(part_1())

def part_2():
    count = 0
    for i in range(0, len(lines), 3):
        common_letters = get_common_letters([lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()])
        if len(common_letters) == 0:
            continue
        count += get_priority(common_letters[0])
    return count

print(part_2())
f = open('test.txt') 
f = open('input.txt')

lines = f.readlines()

def parse(line):
    # 2-4,6-8
    sections = line.split(',')
    ranges = [list(map(int, section.split('-'))) for section in sections]
    return ranges

sections = [parse(line) for line in lines]

def is_overlap_completely(sections):
    s1 = sections[0]
    s2 = sections[1]

    if (s1[0] <= s2[0]) and (s1[1] >= s2[1]):
        return True
    
    if (s2[0] <= s1[0]) and (s2[1] >= s1[1]):
        return True

    return False

def is_partial_overlap(sections):
    s1 = sections[0]
    s2 = sections[1]

    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])

    return start <= end

def part1():
    count = 0
    for section in sections:
        if is_overlap_completely(section):
            count += 1
    return count

def part2():
    count = 0
    for section in sections:
        if is_partial_overlap(section):
            count += 1
    return count

print(part1())
print(part2())
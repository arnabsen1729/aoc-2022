
PART1_RES = 21
PART2_RES = 8

def parse(lines):
    return [[int(x) for x in line.strip()] for line in lines]

def part1(matrix):
    
    m = len(matrix)
    n = len(matrix[0])
    visible = [[0]*n for _ in range(m)]
    # checking from left
    for i in range(m):
        max_so_far = -1
        for j in range(n):
            if matrix[i][j] > max_so_far:
                max_so_far = matrix[i][j]
                visible[i][j] = 1
    
    # checking from top
    for j in range(n):
        max_so_far = -1
        for i in range(m):
            if matrix[i][j] > max_so_far:
                max_so_far = matrix[i][j]
                visible[i][j] = 1

    # checking from right
    for i in range(m):
        max_so_far = -1
        for j in range(n-1, -1, -1):
            if matrix[i][j] > max_so_far:
                max_so_far = matrix[i][j]
                visible[i][j] = 1

    # checking from bottom
    for j in range(n):
        max_so_far = -1
        for i in range(m-1, -1, -1):
            if matrix[i][j] > max_so_far:
                max_so_far = matrix[i][j]
                visible[i][j] = 1

    return sum([sum(x) for x in visible])



def part2(matrix):
    m = len(matrix)
    n = len(matrix[0])

    def get_score(r, c):
        dirs = [0]*4
        for i in range(r-1, -1, -1):
            dirs[0] += 1
            if matrix[i][c] >= matrix[r][c]:
                break
                
        for i in range(r+1, m):
            dirs[1] += 1
            if matrix[i][c] >= matrix[r][c]:
                break
        
        for j in range(c-1, -1, -1):
            dirs[2] += 1
            if matrix[r][j] >= matrix[r][c]:
                break

        for j in range(c+1, n):
            dirs[3] += 1
            if matrix[r][j] >= matrix[r][c]:
                break

        return dirs[0]*dirs[1]*dirs[2]*dirs[3]
    score = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            score = max(score, get_score(i, j))

    return score


def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    matrix = parse(lines)
    assert part1(matrix) == PART1_RES
    assert part2(matrix) == PART2_RES
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    matrix = parse(lines)
    print('Part 1:', part1(matrix))
    print('Part 2:', part2(matrix))
    f.close()

    
if __name__ == '__main__':
    main()
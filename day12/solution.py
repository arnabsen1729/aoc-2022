ANSWER = 31

def parse(lines):
    return [line.strip() for line in lines]

def get_start(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                return (i, j)

def get_end(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'E':
                return (i, j)

def get_elevation(graph):
    m = len(graph)
    n = len(graph[0])
    elevation = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'S':
                elevation[i][j] = 0
            elif graph[i][j] == 'E':
                elevation[i][j] = 25
            else:
                elevation[i][j] = ord(graph[i][j])-ord('a')

    return elevation

def solve(graph):
    m = len(graph)
    n = len(graph[0])

    start = get_start(graph)
    end = get_end(graph)
    elevation = get_elevation(graph)


    visited = [[False for _ in range(n)] for _ in range(m)]
    distance = [[100000000 for _ in range(n)] for _ in range(m)]
    queue = [start]
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = True
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while len(queue) > 0:
        x, y = queue.pop(0)

        if (x, y) == end:
            return distance[x][y]

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            # check if elevation difference is less than 2
            if elevation[nx][ny] - elevation[x][y] >= 2:
                continue
            
            # check if visited
            if visited[nx][ny]:
                continue
        
            distance[nx][ny] = distance[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))

    return -1

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
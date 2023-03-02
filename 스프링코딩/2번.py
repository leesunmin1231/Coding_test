from collections import deque

def checkIndex(node, n, m):
    if node[0] < 0 or node[0] >= n:
        return False
    if node[1] < 0 or node[1] >= m:
        return False
    return True

def getNextList(node):
    return [
        [node[0] + 1, node[1]], 
        [node[0] - 1, node[1]], 
        [node[0], node[1] + 1], 
        [node[0], node[1] - 1],
        [node[0] + 1, node[1] + 1], 
        [node[0] - 1, node[1] + 1], 
        [node[0] + 1, node[1] - 1], 
        [node[0] - 1, node[1] - 1], 
    ]
def checkEnd(node, grid):
    nextList = [x for x in getNextList(node) if checkIndex(x, n, m) and grid[x[1]][x[0]] == "#"]
    bridge = [x for x in nextList if dist[x[1]][x[0]]]
    if len(bridge) == len(nextList) == 2:
        return True
    return False


def bfs(grid, start):
    q = deque()
    q.append(start)
    dist[start[1]][start[0]] = 1
    nodeCount = 0
    while q:
        node = q.popleft()
        print(dist)
        print(node)
        nodeCount += 1
        if checkEnd(node, grid):
            print(node)
            return 0
        print([x for x in getNextList(node) if checkIndex(x, n, m) and grid[x[1]][x[0]] == "#"])
        for next in [x for x in getNextList(node) if checkIndex(x, n, m) and grid[x[1]][x[0]] == "#"]:
            if dist[next[1]][next[0]]: # 이미 방문한 곳
                continue
            q.append(next)
            dist[next[1]][next[0]] = dist[node[1]][node[0]] + 1
    return nodeCount


def solution(grid):
    global n,m,dist
    n = len(grid[0])
    m = len(grid)
    ans = 0
    dist = [[0] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "#" and not dist[row][col]:
                nodeCount = bfs(grid, [row, col])
                ans += nodeCount

grid = [".#.","#..",".#."]
solution(grid)
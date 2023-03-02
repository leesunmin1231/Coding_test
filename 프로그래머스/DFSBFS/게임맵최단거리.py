from collections import deque

def checkIndex(node, n, m):
    if node[0] < 0 or node[0] >= n:
        return False
    if node[1] < 0 or node[1] >= m:
        return False
    return True

def getNextList(node):
    return [[node[0] + 1, node[1]], [node[0] - 1, node[1]], [node[0], node[1] + 1], [node[0], node[1] - 1]]

def bfs(maps):
    q = deque()
    q.append([0,0])
    answerList = []
    n = len(maps[0])
    m = len(maps)
    dist = [[0] * n for _ in range(m)]
    while q:
        node = q.popleft()
        if node == [n - 1, m - 1]:
            answerList.append(dist[node[1]][node[0]])
        for next in [x for x in getNextList(node) if checkIndex(x, n, m) and maps[x[1]][x[0]]]:
            if dist[next[1]][next[0]]: # 이미 방문한 곳
                continue
            q.append(next)
            dist[next[1]][next[0]] = dist[node[1]][node[0]] + 1
    return answerList
    
def solution(maps):
    answer = bfs(maps)
    if len(answer) == 0:
        return -1
    return min(answer)+1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))
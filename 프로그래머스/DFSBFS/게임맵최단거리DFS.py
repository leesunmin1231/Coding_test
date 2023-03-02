import copy

def checkIndex(node, n, m):
    if node[0] < 0 or node[0] >= n:
        return False
    if node[1] < 0 or node[1] >= m:
        return False
    return True

def getNextList(node):
    return [[node[0] + 1, node[1]], [node[0] - 1, node[1]], [node[0], node[1] + 1], [node[0], node[1] - 1]]

def dfs(maps, pre_dist, node):
    if node == [n+1, m+1]:
        answer.append(pre_dist[node[1]][node[0]])
        return
    dist = copy.deepcopy(pre_dist)
    for next in [x for x in getNextList(node) if checkIndex(x, n, m) and maps[x[1]][x[0]]]:
        if dist[next[1]][next[0]]: # 이미 방문한 곳
            continue
        dist[next[1]][next[0]] = dist[node[1]][node[0]] + 1
        dfs(maps, dist, next)
    
def solution(maps):
    global answer, n, m
    answer = []
    n = len(maps[0])
    m = len(maps)
    dist = [[0] * n for _ in range(m)]
    dist[0][0] = 1
    dfs(maps, dist, [0,0])
    if len(answer) == 0:
        return -1
    return min(answer)


maps = [[1, 1], [1, 1], [1, 1]]
print(solution(maps))
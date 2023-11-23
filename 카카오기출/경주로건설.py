from collections import deque
import sys

def solution(board):
    INF=sys.maxsize
    q = deque()
    dr = [-1, 0, 1, 0] # 위, 오른쪽, 아래, 왼쪽
    dc = [0, 1, 0, -1]
    q.append([0, 0, 2])
    q.append([0, 0, 1])
    N = len(board)
    costs = [[[INF] * N for _ in range(N)] for _ in range(4)]
    ans = INF
    for i in range(4):
        costs[i][0][0] = 0
    while q:
        r, c, d = q.popleft()
        if r == N-1 and c == N-1:
            result = costs[d][r][c]
            if result < ans:
                ans = result
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nd = i
            if nr < 0 or nr >= N:
                continue
            if nc < 0 or nc >= N:
                continue
            if board[nr][nc] == 1:
                continue
            newCost = costs[d][r][c] + 100
            if d!=nd:
                newCost += 500
            if newCost < costs[nd][nr][nc]:
                costs[nd][nr][nc] = newCost
                q.append([nr, nc, nd])
    return ans

print(solution([
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0]
]))
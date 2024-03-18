import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(" "))
board = [[0] * n for _ in range(n)]
dist = [0] * n
for _ in range(m):
    r,c = map(int, input().split(" "))
    board[r-1][c-1] = 1
    board[c-1][r-1] = 1

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if dist[node]:
            continue
        dist[node] = 1
        for next in [index for index, x in enumerate(board[node]) if x]:
            if dist[next]:
                continue
            q.append(next)

ans = 0
for i in range(n):
    if not dist[i]:
        bfs(i)
        ans += 1
print(ans)
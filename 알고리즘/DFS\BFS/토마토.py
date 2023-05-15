import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

q = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            q.append([r,c])
dist = [[0] * M for _ in range(N)]
ans = -1
while q:
    node = q.popleft()
    board[node[0]][node[1]] = 1
    ans = dist[node[0]][node[1]]
    for next in [[node[0]-1, node[1]], [node[0], node[1]-1], [node[0]+1, node[1]], [node[0], node[1]+1]]:
        if next[0] < 0 or next[0] >= N:
            continue
        if next[1] < 0 or next[1] >= M:
            continue
        if board[next[0]][next[1]] == 1:
            continue
        if board[next[0]][next[1]] == -1:
            continue
        if dist[next[0]][next[1]]:
            continue
        q.append(next)
        dist[next[0]][next[1]] = dist[node[0]][node[1]] + 1
flag = True
for r in range(N):
    for c in range(M):
        if not board[r][c]:
            flag = False
if flag:
    print(ans)
else:
    print(-1)
        
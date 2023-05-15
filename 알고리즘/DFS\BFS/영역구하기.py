import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int,input().split(" "))

def bfs(start, board):
    q = deque()
    q.append(start)
    size = 0
    while q:
        r, c = q.popleft()
        if board[r][c]:
            continue
        board[r][c] = 1
        size += 1
        for next in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
            nr,nc = next
            if nr < 0 or nc < 0:
                continue
            if nr >= N or nc >= M:
                continue
            if board[nr][nc]:
                continue
            q.append(next)
    return size

blocks = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split(" "))
    blocks.append([[x1, y1], [x2,y2]])
board = [[0] * M for _ in range(N)]
for block in blocks:
    left, right = block
    r1, c1 = left
    r2, c2 = right
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1
ans = 0
sizes = []
for r in range(N):
    for c in range(M):
        if not board[r][c]:
            sizes.append(bfs([r,c], board))
            ans += 1
print(ans)
print(' '.join(list(map(str, sorted(sizes)))))
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


def bfs(start, board, visited):
    q = deque()
    q.append(start)
    size = 0
    while q:
        r, c = q.popleft()
        if not board[r][c]:
            continue
        if visited[r][c]:
            continue
        visited[r][c] = 1
        size += 1
        for next in [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]:
            nr, nc = next
            if nr < 0 or nc < 0:
                continue
            if nr >= N or nc >= N:
                continue
            if not board[nr][nc]:
                continue
            if visited[nr][nc]:
                continue
            q.append(next)
    return size

board = []
for _ in range(N):
    board.append(list(map(int, list(input())[:-1])))

visited = [[0] * N for _ in range(N)]
sizes = []
for r in range(N):
    for c in range(N):
        if board[r][c] and not visited[r][c]:
            sizes.append(bfs([r,c], board, visited))
sizes.sort()
print(len(sizes))
for size in sizes:
    print(size)
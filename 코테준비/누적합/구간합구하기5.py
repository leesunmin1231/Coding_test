import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = [[0] * (N+1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split(" "))))
tmp = [[0] * (N+1) for _ in range(N+1)]

for r in range(1,N+1):
    for c in range(1,N+1):
        tmp[r][c] = board[r][c] + tmp[r-1][c] + tmp[r][c-1] - tmp[r-1][c-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split(" "))
    print(tmp[x2][y2] - tmp[x2][y1-1] - tmp[x1-1][y2] + tmp[x1-1][y1-1])



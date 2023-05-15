import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split(" "))
boards = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split(" "))))
    boards.append(tmp)

q = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if boards[h][r][c] == 1:
                q.append([h,r,c])

dist = [[[0] * M for _ in range(N)] for _ in range(H)]
visit = [[[0] * M for _ in range(N)] for _ in range(H)]
ans = -1
while q:
    node = q.popleft()
    visit[node[0]][node[1]][node[2]] = 1
    ans = dist[node[0]][node[1]][node[2]]
    for next in [[node[0]+1, node[1], node[2]], [node[0]-1, node[1], node[2]], [node[0], node[1]+1, node[2]], [node[0], node[1]-1, node[2]], [node[0], node[1], node[2]+1], [node[0], node[1], node[2]-1]]:
        if next[0] < 0 or next[1] < 0 or next[2] < 0:
            continue
        if next[0] >= H or next[1] >= N or next[2] >= M:
            continue
        h,r,c = next
        if visit[h][r][c]:
            continue
        if boards[h][r][c] != 0:
            continue
        dist[h][r][c] = dist[node[0]][node[1]][node[2]] + 1
        boards[h][r][c] = 1
        q.append(next)

flag = True
for h in range(H):
    for r in range(N):
        for c in range(M):
            if boards[h][r][c] == 0:
                flag = False
if flag:
    print(ans)
else:
    print(-1)
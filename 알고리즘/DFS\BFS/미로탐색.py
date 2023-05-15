import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(map(int, list(input())[:-1])))

q = deque()
q.append([0,0])
dist = [[0] * M for _ in range(N)]
dist[0][0] = 1
while q:
    node = q.popleft()
    if node == [N-1, M-1]:
        break
    for next in [[node[0]-1, node[1]],[node[0], node[1]-1],[node[0]+1, node[1]],[node[0], node[1]+1]]:
        if next[0] >= N or next[0] < 0:
            continue
        if next[1] >= M or next[1] < 0:
            continue
        if not board[next[0]][next[1]]:
            continue
        if dist[next[0]][next[1]]:
            continue
        q.append(next)
        dist[next[0]][next[1]] = dist[node[0]][node[1]] + 1
print(dist[N-1][M-1])

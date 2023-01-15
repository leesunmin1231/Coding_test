import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
planet = []
for _ in range(N):
    row = list(map(int, input().split()))
    planet.append(row)

def getNextPos(next):
    x = next[0]
    y = next[1]
    if (next[0] < 0):
        x = N-1
    if (next[0] >= N):
        x = 0
    if (next[1] < 0):
        y = M -1
    if (next[1] >= M):
        y = 0
    return [x,y]

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if (planet[node[0]][node[1]]):
            continue
        planet[node[0]][node[1]] = 1
        for next in (getNextPos([node[0]+1, node[1]]),getNextPos([node[0]-1, node[1]]),getNextPos([node[0], node[1]+1]),getNextPos([node[0], node[1]-1])):
            if not planet[next[0]][next[1]]:
                queue.append(next)

count = 0
for rowIdx in range(N):
    for colIdx in range(M):
        if (planet[rowIdx][colIdx]):
            continue
        if not (planet[rowIdx][colIdx]):
            bfs([rowIdx,colIdx])
            count+=1
print(count)
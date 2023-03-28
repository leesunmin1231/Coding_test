import sys
from collections import deque

def path(node):
    pathArr = []
    tmp = node
    for _ in range(dist[node] + 1):
        pathArr.append(tmp)
        tmp = move[tmp]
    return (' '.join(map(str, reversed(pathArr))))

def bfs():
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if node == end:
            print(dist[node])
            print(path(node))
            break
        for next in (node - 1, node + 1, node*2):
            if (0<=next <= MAX) and not dist[next]:
                q.append(next)
                dist[next] = dist[node]+1
                move[next] = node



MAX = 10**5
dist = [0]*(MAX+1)
move = [0]*(MAX+1)
start, end = map(int, sys.stdin.readline().rstrip().split())
bfs();
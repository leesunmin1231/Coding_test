import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(V)
    while q:
        node = q.popleft()
        if (visit_bfs[node]):
            continue
        visit_bfs[node] = True
        path_bfs.append(node)
        for next in [index for index, x in enumerate(graph[node]) if x]:
            q.append(next)

def dfs(node):
    visit_dfs[node] = True
    path_dfs.append(node)
    for next in [index for index, x in enumerate(graph[node]) if x]:
        if not visit_dfs[next]:
            dfs(next)


N, M, V = map(int, input().split(" "))
graph = [[0]*(N+1) for _ in range(N+1)]
visit_bfs = [False]*(N+1)
visit_dfs = [False]*(N+1)
path_bfs = []
path_dfs = []
for _ in range(M):
    one, two = map(int, input().split(" "))
    graph[one][two] = 1
    graph[two][one] = 1
dfs(V)
for x in path_dfs:
    print(x, end=" ")
print("")
bfs()
for x in path_bfs:
    print(x, end=" ")
print("")
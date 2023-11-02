import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = {}
visited = {}
for _ in range(m):
    a,b,c = map(int,input().split(" "))
    if a in graph:
        graph[a].append([c,b])
    else:
        graph[a] = [[c,b]]
    if b in graph:
        graph[b].append([c,a])
    else:
        graph[b] = [[c,a]]

heap = [[0,1]]
result = []
while heap:
    price, node = heapq.heappop(heap)
    if node in visited and visited[node]:
        continue
    visited[node] = True
    result.append(price)
    for next in graph[node]:
        heapq.heappush(heap, next)
print(sum(result) - max(result))
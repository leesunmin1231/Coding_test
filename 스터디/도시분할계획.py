import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split(" "))
    graph[a].append([c,b])
    graph[b].append([c,a])

heap = [[0,1]]
result = []
while heap:
    price, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    result.append(price)
    if len(result) == n:
        break
    for next in graph[node]:
        heapq.heappush(heap, next)
print(sum(result) - max(result))
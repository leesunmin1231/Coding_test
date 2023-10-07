import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split(" "))
k = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split(" "))
    edges[u].append([w, v])

distance = [INF] * (V+1)

def dijkstra():
    q = []
    heapq.heappush(q, [0, k])
    distance[k] = 0
    while q:
        cost, dest = heapq.heappop(q)
        if distance[dest] < cost:
            continue
        for ncost, ndest in edges[dest]:
            if ncost+cost < distance[ndest]:
                distance[ndest] = ncost+cost
                heapq.heappush(q, [ncost+cost, ndest])

dijkstra()

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
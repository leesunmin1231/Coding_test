import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split(" "))
edges = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int,input().split(" "))
    edges[a].append([c, b])
    edges[b].append((c, a))

v1, v2 = map(int, input().split(" "))
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n+1)
    q = [(0,start)]
    distance[start] = 0
    while q:
        cost, dest = heapq.heappop(q)
        if distance[dest] < cost:
            continue
        for nCost, nDest in edges[dest]:
            if nCost + cost < distance[nDest]:
                heapq.heappush(q, (nCost + cost, nDest))
                distance[nDest] = cost + nCost
    return distance

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
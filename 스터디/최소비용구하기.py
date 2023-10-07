import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int,input().split(" "))
    edges[a].append([c, b])

start, end = map(int, input().split(" "))

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        cost, dest = heapq.heappop(q)
        if distance[dest] < cost:
            continue
        for next_cost, next_dest in edges[dest]:
            if next_cost + cost < distance[next_dest]:
                heapq.heappush(q, [next_cost+ cost, next_dest])
                distance[next_dest] = next_cost+cost

                

dijkstra(start)
print(distance[end])
import sys
import heapq
import math

input = sys.stdin.readline

n = int(input())
nodes = []
for _ in range(n):
    x, y = map(float, input().split(" "))
    nodes.append((x,y))

visit = {}

q = [(0, nodes[0])]
ans = 0
while q:
    d, node = heapq.heappop(q)
    if node in visit and visit[node]:
        continue
    visit[node] = True
    ans += d
    for next in [x for x in nodes if x != node]:
        distance = round(math.sqrt((next[0]-node[0])**2 + (next[1] - node[1])**2), 2)
        heapq.heappush(q, (distance, next))
print(round(ans, 2))

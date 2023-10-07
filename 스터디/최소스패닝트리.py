import sys

input = sys.stdin.readline

v, e = map(int, input().split(" "))
edgeList = []
for _ in range(e):
    a,b,c = map(int,input().split(" "))
    edgeList.append([a,b,c])
edgeList.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]

def find(target):
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot < bRoot:
        parent[bRoot] = aRoot
    else:
        parent[aRoot] = bRoot

ans = 0
for a,b,c in edgeList:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)


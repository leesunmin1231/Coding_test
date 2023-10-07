import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

edgeList = []
for _ in range(m):
    a,b,c = map(int,input().split(" "))
    edgeList.append([a,b,c])

edgeList.sort(key=lambda x: x[2])
parent = [i for i in range(n+1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    aRoot = find(a)
    bRoot = find(b)
    if bRoot < aRoot:
        parent[aRoot] = bRoot
    else:
        parent[bRoot] = aRoot

result = []
for a,b,c in edgeList:
    if find(a) != find(b):
        union(a,b)
        result.append(c)

print(sum(result)-max(result))
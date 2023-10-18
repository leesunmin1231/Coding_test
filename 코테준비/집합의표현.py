import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int,input().split(" "))
arr = []
for i in range(n+1):
    arr.append(i)

def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootB != rootA:
        arr[rootA] = rootB

for _ in range(m):
    cmd, a, b = map(int, input().split(" "))
    if cmd == 0:
        union(a,b)
    else:
        rootA = find(a)
        rootB = find(b)
        if rootA == rootB:
            print("yes")
        else:
            print("no")
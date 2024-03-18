import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(int(input()))

seg_tree = [0]* (1 << (int(math.ceil(math.log2(N))) + 1))

def build(start, end, x):
    if start == end:
        seg_tree[x] = arr[start]
        return seg_tree[x]
    mid = (start + end )// 2
    left = build(start, mid, x*2)
    right = build(mid+1, end, x*2 + 1)
    seg_tree[x] = (left*right)%1000000007
    return seg_tree[x]

def find(b, c, start, end, x):
    if start > c or end < b:
        return 1
    elif start >= b and end <= c:
        return seg_tree[x]
    mid = (start+end)//2
    left = find(b,c, start, mid, x*2)
    right = find(b,c, mid+1,end, x*2+1)
    return (left*right)%1000000007

def update(target, newNum, start, end, x):
    if start > target or end < target:
        return
    elif start == end == target:
        seg_tree[x] = newNum
        return
    mid = (start+end)//2
    update(target, newNum, start, mid, x*2)
    update(target, newNum, mid+1, end, x*2+1)
    seg_tree[x] = (seg_tree[x*2] * seg_tree[x*2+1])%1000000007

build(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split(" "))
    if a == 1:
        update(b-1, c, 0, N-1, 1)
    else:
        ans = find(b-1, c-1, 0, N-1, 1)
        print(ans)
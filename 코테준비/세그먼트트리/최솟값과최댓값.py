import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(int(input()))

seg_tree = [0] * (N*4)

def build(start, end, x):
    if start == end:
        seg_tree[x] = [arr[start], arr[start]]
        return seg_tree[x]
    mid = (start + end) // 2
    left = build(start, mid, x*2)
    right = build(mid+1, end, x*2+1)
    seg_tree[x] = [min(left[0],right[0]), max(left[1], right[1])]
    return seg_tree[x]

def find(a,b, start, end, x):
    if a > end or b < start:
        return [1000000001, 0]
    if start >= a and end <= b:
        return seg_tree[x]
    mid = (start + end) // 2
    left = find(a,b, start, mid, x*2)
    right = find(a, b, mid+1, end, x*2+1)
    return [min(left[0],right[0]), max(left[1], right[1])]

build(0, N-1, 1)

for _ in range(M):
    a, b = map(int, input().split(" "))
    minNum, maxNum = find(a-1, b-1, 0, N-1, 1)
    print(minNum, maxNum)

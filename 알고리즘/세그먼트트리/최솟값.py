import sys

input = sys.stdin.readline

n , m = map(int, input().split(" "))
arr = []
for _ in range(n):
    arr.append(int(input()))

seg_tree = [0] * (n*4)

def build(start, end, x):
    if start == end:
        seg_tree[x] = arr[start]
        return seg_tree[x]
    mid = (start + end) // 2
    left = build(start, mid, x*2)
    right = build(mid+1, end, x*2+1)
    seg_tree[x] = min(left, right)
    return seg_tree[x]

def find(a, b, start, end, x):
    if start > b or end < a:
        return 10000000001
    elif start >= a and end <= b:
        return seg_tree[x]
    mid = (start + end) // 2
    left = find(a, b, start, mid, x*2)
    right = find(a, b, mid+1, end, x*2+1)
    return min(left, right)

build(0,n-1, 1)

for _ in range(m):
    a, b = map(int, input().split(" "))
    print(find(a-1, b-1, 0, n-1, 1))

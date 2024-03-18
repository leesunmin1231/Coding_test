import sys

input = sys.stdin.readline

N, M, K = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(int(input()))

segment_tree = [0] * (N*4)

def build_tree(start, end, x):
    if start == end:
        segment_tree[x] = arr[start]
        return arr[start]
    mid = (start+end) // 2
    left_sum = build_tree(start, mid, x*2)
    right_sum = build_tree(mid+1, end, x*2+1)
    segment_tree[x] = left_sum + right_sum
    return segment_tree[x]

def find_tree(b, c, start, end, x):
    if b > end or c < start:
        return 0
    if b <= start and c >= end:
        return segment_tree[x]
    mid = (start+end) // 2
    left = find_tree(b,c, start, mid, x*2)
    right = find_tree(b,c, mid+1, end, x*2+1)
    return left+right

def update_tree(target, new_num, start, end, x):
    if target > end or target < start:
        return
    if start == end == target:
        segment_tree[x] = new_num
        return
    mid = (start + end) // 2
    update_tree(target, new_num, start, mid, x*2)
    update_tree(target, new_num, mid+1, end, x*2+1)
    segment_tree[x] = segment_tree[x*2] + segment_tree[x*2+1]

build_tree(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split(" "))
    if a == 1:
        # 숫자 바꾸기
        update_tree(b-1, c, 0, N-1, 1)
    elif a == 2:
        # b, c까지 구간 합 구하여 출력
        ans = find_tree(b-1, c-1, 0, N-1, 1)
        print(ans)
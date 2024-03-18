import sys

input = sys.stdin.readline
N, M, L = map(int, input().split(" "))
arr = []
if (N != 0):
    arr = list(map(int, input().split(" ")))
else:
    input()
arr.sort();
arr.append(L)
left = 1
right = L
while left <= right:
    mid = (left + right) // 2
    prev = arr[0]
    count = 0
    if prev > mid:
        count += (prev-1) // mid
    for i in range(1, N+1):
        if arr[i] > prev + mid:
            count += (arr[i] - prev-1) // mid
        prev = arr[i]
    if count > M:
        left = mid+1
    else:
        right = mid-1
print(left)
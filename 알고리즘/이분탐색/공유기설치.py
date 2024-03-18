import sys

input = sys.stdin.readline

N, C = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
maxD = arr[N-1] - arr[0]
minD = 1

while minD <= maxD:
    mid = (minD + maxD) // 2
    start = arr[0]
    next = start+mid
    count = 1
    for j in range(1, N):
        if arr[j] >= next:
            next = arr[j] + mid
            count += 1
    if count >= C:
        minD = mid+1
    else:
        maxD = mid-1
print(maxD)
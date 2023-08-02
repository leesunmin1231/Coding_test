import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
start = 0
end = 1
result = 10000
while end < N:
    if arr[end] - arr[start] < 4:
        end += 1
        continue
    elif arr[end] - arr[start] == 4:
        if result > 4 - (end-start):
            result = 4 - (end-start)
    elif arr[end] - arr[start] > 4:
        if result > 5 - (end-start):
            result = 5 - (end-start)
    start+=1
    if start == end:
        end+=1
if arr[end-1] - arr[start] < 4:
    if result > 4 - (end-1-start):
        result = 4-(end-1-start)
print(result)

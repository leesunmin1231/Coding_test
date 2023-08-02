import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
start = 0
end = 0
tmp = arr[start]
count = 0
while end < N:
    if tmp < M:
        end+=1
        if end == N: break
        tmp+=arr[end]
        continue
    if tmp == M:
        count+=1
    tmp-=arr[start]
    start+=1
    if end < start:
        end+=1
        if end == N: break
        tmp+=arr[end]
print(count)
    
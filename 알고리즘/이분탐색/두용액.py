import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

start = 0
end = N-1
totalSum = arr[start] + arr[end]
ans = [arr[start], arr[end]]
while start < end:
    if abs(arr[start]+ arr[end] - 0) < abs(totalSum - 0):
        totalSum = arr[start] + arr[end]
        ans = [arr[start], arr[end]]
    if arr[start] + arr[end] < 0:
        start+=1
    else:
        end -= 1
print(ans[0], ans[1])
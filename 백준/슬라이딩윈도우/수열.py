import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
start = 0
end = K-1
ans = -1000000000
tmp = sum(nums[start: end+1])
while end < N-1:
    if tmp > ans:
        ans = tmp
    tmp = tmp - nums[start] + nums[end+1]
    start += 1
    end += 1
if tmp > ans:
    ans = tmp
print(ans)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
ans = 0
arr.sort(reverse=True)
count = 0
while count < M:
    for i in range(K):
        count += 1
        ans += arr[0]
    ans += arr[1]
    count += 1

print(ans)
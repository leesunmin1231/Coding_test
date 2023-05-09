import sys

input = sys.stdin.readline

A, B = map(int, input().split(" "))
ans = 1
while True:
    if A == B:
        break
    if B % 2 ==0:
        B = B//2
        ans += 1
        continue
    if B == 1 and A != B:
        ans = -1
        break
    if str(B)[-1] == '1':
        B = int(str(B)[:-1])
        ans += 1
        continue
    else:
        ans = -1
        break
print(ans)
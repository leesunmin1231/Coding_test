import sys

input = sys.stdin.readline

N = int(input())
ans = -1
pack = N // 5
rest = N % 5
while rest <= N:
    if rest % 3 == 0:
        ans = pack + rest // 3
        break
    pack -= 1
    rest += 5
print(ans)
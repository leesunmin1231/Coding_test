import sys

input = sys.stdin.readline

K = bin(int(input()))[2:] #2진법으로 변환하여 풀이
b = format(value, 'b')
ans = 0

for i, num in enumerate(K):
    if (int(num) == 1):
        ans += 3**(len(K) - i -1)
print(ans)
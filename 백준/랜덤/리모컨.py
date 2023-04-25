import sys
from itertools import product

input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    broken = input()[:-1].split(" ")
else:
    broken = []

def possible_num(x, broken):
    x = list(str(x))
    for element in x:
        if element in broken:
            return False
    return True

def solution(N, broken):
    answer = abs(N - 100)

    for temp in range(1000001):
        if possible_num(temp, broken):
            answer = min(answer, len(str(temp)) + abs(N-temp))
    return answer

print(solution(N, broken))
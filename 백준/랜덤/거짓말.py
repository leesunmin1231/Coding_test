import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split(" "))

truth = list(map(int, input().split(" ")[1:]))
party = []
for _ in range(M):
    people = list(map(int, input().split(" ")[1:]))
    party.append(people)

check = [False] * M
q = deque(truth)
while q:
    truep = q.popleft()
    for i,people in enumerate(party):
        if truep in people:
            check[i] = True
            for a in people:
                if a not in truth:
                    q.append(a)
                    truth.append(a)
print(len([x for x in check if not x]))
    
        

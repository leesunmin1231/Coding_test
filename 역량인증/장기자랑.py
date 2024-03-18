# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N, S, M = map(int, readl().split())
	return N, S, M


sol_list = []

# 입력받는 부분
N, S, M = input_data()
# q = deque()
# for i in range(1, N+1):
# 	q.append(i)
# while q[0] != S:
# 	q.append(q.popleft())
# for i in range(N):
# 	for j in range(1,M):
# 		q.append(q.popleft())
# 	print(q.popleft(), end=" ")

A = list(range(1, N+1))
ans = []
idx = (S-1)%N
while A:
	idx = (idx - 1 + M)%len(A)
	ans.append(str(A.pop(idx)))
print(" ".join(ans))

import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	A = [int(x) for x in readl().split()]

	return N, A

# 입력
# N: 후보자 수
# A: 기질 값
N, A = InputData()

# 코드를 작성하세요
tmp = 10 ** 9
ans = []

start = 0
end = N-1
while start < end:
	if abs(A[start] + A[end]) < tmp:
		tmp = abs(A[start] + A[end])
		ans = [start, end]
	if A[start] + A[end] == 0:
		break
	elif A[start] + A[end] < 0:
		start += 1
	else:
		end -= 1

print(' '.join(map(str, ans)))
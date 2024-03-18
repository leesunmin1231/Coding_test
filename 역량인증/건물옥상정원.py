import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	H = [ int(readl()) for i in range(N) ]
	return N, H


# 입력
# N: 건물 수
# H: 건물 높이
N, H = InputData()

# 코드를 작성 하세요
d = [i for i in range(N-1, -1, -1)]
stack = []
stack.append(0)
ans = []
for i in range(1,N):
    while stack and H[stack[-1]] <= H[i]:
        tmp = stack.pop()
        d[tmp] = i - tmp - 1
    stack.append(i)

# 출력
print(sum(d))
 
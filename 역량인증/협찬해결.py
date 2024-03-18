import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D


def Solve():
	sol = -30001#첫번째 방법의 최대 선호도
	sumnums = 0
	for i in range(N):
		if (sumnums > 0 ):
			sumnums+= D[i]
		else:
			sumnums = D[i];
		if (sol < sumnums):
			sol = sumnums
	return sol

#입력받는 부분
N, D = input_data()
sol = Solve()
print(sol)#출력하는 부분
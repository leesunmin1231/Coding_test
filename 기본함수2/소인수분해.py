# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
import math
N = int(input())
q = N # 몫
while q != 1:
    flag = 0
    if q % 2 == 0:
        print(2)
        q = q//2
        continue
    else:
        for i in range(3, int(math.sqrt(N))+ 1, 2):
            if q % i == 0:
                print(i)
                flag = 1
                q= q//i
                break
        if flag == 0:
            print(q)
            q = 1
    
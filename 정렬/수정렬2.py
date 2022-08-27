# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

def bucket_sort(lst):
    n = len(lst) // 2 + 1
    min_num = min(lst)
    max_num = max(lst)
    B = [0 for i in range(n)]
    term = (max_num - min_num) // (n-1)
    for num in lst:
        idx = (num - min_num) // term
        if B[idx] != 0:
            B[idx].append(num)
        else:
            B[idx] = [num]
    for i in range(n):
        B[i].sort()
    return B

import sys
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in lst:
    print(i)


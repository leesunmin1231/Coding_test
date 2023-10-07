from itertools import combinations

n = int(input())
arr = []
for i in range(n):
    t, p = map(int, input().split(" "))
    arr.append((t,p, i+1))

tmp = []
for i in range(1,n+1):
    tmp.extend(list(combinations(arr, i)))

def isImpossible(arr):
    prev = arr[0]
    result = prev[1]
    length = len(arr)
    if prev[0] + prev[2] - 1 > n:
        return 0
    for i in range(1, length):
        cur = arr[i]
        if prev[0] + prev[2] - 1 >= cur[2]:
            return 0
        if cur[0] + cur[2] - 1 > n:
            return 0
        result += cur[1]
        prev = cur
    return result

ans = []
for kind in tmp:
    # 불가능한 경우 거르기
    tmp = isImpossible(kind)
    if tmp == 0:
        continue
    # 가능한 경우 돈계산
    ans.append(tmp)

if len(ans) == 0:
    print(0)
else:
    print(max(ans))
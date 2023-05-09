import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        score = tuple(map(int, input().split(" ")))
        arr.append(score)
    ans = 1
    arr.sort(key=lambda x:x[0])
    maxScore = arr[0][1]
    for score in arr:
        if score == arr[0]:
            continue
        if score[1] < maxScore:
            maxScore = score[1]
            ans +=1
    print(ans)

import sys

input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    ops = list(input())[:-1]
    n = int(input())
    if n == 0:
        input()
        result.append("error")
        continue
    nums = list(map(int, input()[1:-2].split(",")))
    ans = nums[:]
    for op in ops:
        if op == "R":
            ans.reverse()
        elif op == "D":
            if len(ans) == 0:
                ans = "error"
                break
            ans = ans[1:]
    result.append(ans)
    
for ans in result:
    print(ans)
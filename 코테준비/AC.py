import sys
from collections import deque

input = sys.stdin.readline

def calculate(nums, cmds):
    isReverse = False
    q = deque(nums)
    for cmd in list(cmds):
        if cmd == "R":
            if isReverse:
                isReverse = False
            else:
                isReverse = True
        else:
            if not q:
                return "error"
            if isReverse:
                q.pop()
            else:
                q.popleft()
    ans = list(q)
    if isReverse:
        ans.reverse()
    return "[" + ','.join(list(map(str, ans))) + ']'


T = int(input())
for _ in range(T):
    cmd = input().strip()
    n = int(input())
    tmp = input().strip()[1:-1].split(",")
    if n == 0 and 'D' in cmd:
        print("error")
        continue
    elif n == 0:
        print("[]")
        continue
    nums = list(map(int, tmp))
    ans = calculate(nums, cmd)
    print(ans)
import sys

input = sys.stdin.readline

N, L = map(int, input().split(" "))

board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def isSameNum(arr):
    check = arr[0]
    for i in arr:
        if i != check:
            return False
    return True

def canUseLayer(arr, L):
    prev = 0
    cur = 1
    while cur < N:
        if arr[prev] == arr[cur]:
            cur += 1
            continue
        elif arr[prev] < arr[cur]:
            if arr[cur] - arr[prev] != 1:
                return False
            if cur - prev < L:
                return False
            prev = cur
            cur += 1
        else:
            if arr[prev] - arr[cur] != 1:
                return False
            prev = cur
            i = 0
            while i < L:
                if cur+i >= N:
                    return False
                if arr[prev] != arr[cur+i]:
                    return False
                i += 1
            prev += L
            cur = prev + 1
            if prev < N and arr[prev] > arr[prev-1]:
                return False
            if prev < N and arr[prev] < arr[prev-1]:
                prev -= 1
                cur -= 1
    return True
        

ans = 0
# row 검사
for row in board:
    if isSameNum(row):
        ans += 1
    elif canUseLayer(row, L):
        ans += 1

for c in range(N):
    col = []
    for r in range(N):
        col.append(board[r][c])
    if isSameNum(col):
        ans += 1
    elif canUseLayer(col, L):
        ans += 1

print(ans)
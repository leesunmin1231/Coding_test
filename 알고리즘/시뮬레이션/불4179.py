import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split(" "))
board = []
for _ in range(R):
    board.append(list(input())[:-1])
q = deque()
fire = deque()

def init():
    for r in range(R):
        for c in range(C):
            if board[r][c] == "J":
                q.append([r,c, 1])
            elif board[r][c] == "F":
                fire.append([r,c])

def spreadFire():
    size = len(fire)
    for i in range(size):
        r,c = fire.popleft()
        for next in [[r+1, c], [r-1,c],[r,c+1],[r,c-1]]:
            nr, nc = next
            if nr < 0 or nr >= R:
                continue
            if nc < 0 or nc >= C:
                continue
            if board[nr][nc] == "#":
                continue
            if board[nr][nc] == "F":
                continue
            board[nr][nc] = "F"
            fire.append([nr,nc])


def bfs():
    checkTime = 0
    while q:
        r, c, count = q.popleft()
        board[r][c] = "J"
        # end 조건 체크
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            return count
        if checkTime < count:
            spreadFire()
            checkTime = count
        # J이동
        for next in [[r+1, c], [r-1,c],[r,c+1],[r,c-1]]:
            nr, nc = next
            if nr < 0 or nr >= R:
                continue
            if nc < 0 or nc >= C:
                continue
            if board[nr][nc] == "#":
                continue
            if board[nr][nc] == "F":
                continue
            if board[nr][nc] == "J":
                continue
            q.append([nr, nc, count+1])
    return "IMPOSSIBLE"


init()
print(bfs())
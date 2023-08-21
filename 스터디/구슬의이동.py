# 코드트리


import sys

input = sys.stdin.readline

n, m, t, k = map(int, input().split(" "))
balls = []

for _ in range(m):
    r, c, d, v = input().split(" ")
    balls.append([int(r)-1, int(c)-1, d, int(v)])

board = [[[] for _ in range(n)] for _ in range(n)]

def init():
    for index, ball in enumerate(balls):
        r, c, d, v = ball
        board[r][c].append(index)

def moveball(r,c,d,v):
    v = v % ((n-1) * 2)
    if d == "L":
        nc = c
        while v > 0:
            if (nc == 0):
                break
            nc -= 1
            v -= 1
        while v > 0:
            if (nc == n-1):
                break
            d = 'R'
            nc += 1
            v -= 1
        while v > 0:
            d = "L"
            nc -= 1
            v -= 1
        return [r, nc, d]
    if d == "R":
        nc = c
        while v > 0:
            if (nc == n-1):
                break
            nc += 1
            v -= 1
        while v > 0:
            if (nc == 0):
                break
            d = "L"
            nc -= 1
            v -= 1
        while v > 0:
            d = "R"
            nc += 1
            v -= 1
        return [r,nc, d]
    if d == "U":
        nr = r
        while v > 0:
            if (nr == 0):
                break
            nr -= 1
            v -= 1 
        while v > 0:
            if (nr == n-1):
                break
            d = "D"
            nr += 1
            v -= 1
        while v > 0:
            d = "U"
            nr -= 1
            v -= 1
        return [nr, c, d]
    if d == "D":
        nr = r 
        while v > 0:
            if (nr == n-1):
                break
            nr += 1
            v -= 1 
        while v > 0:
            if (nr == 0):
                break
            d = "U"
            nr -= 1
            v -= 1
        while v > 0:
            d = "D"
            nr += 1
            v -= 1
        return [nr, c, d]

def solution(board, balls):
    init()
    for clock in range(t):
        # 공 이동 시키기
        for index, ball in enumerate(balls):
            r,c,d,v = ball
            if index not in board[r][c]:
                continue
            board[r][c].remove(index)
            nr, nc, nd = moveball(r,c,d,v)
            board[nr][nc].append(index)
            balls[index] = [nr, nc, nd, v]
        # 한칸에 있는 공 개수 체크
        for r in range(n):
            for c in range(n):
                if len(board[r][c]) > k:
                    tmp = []
                    for i in board[r][c]:
                        r,c,d,v = balls[i]
                        tmp.append([i, v])
                    tmp.sort(key=lambda x: (x[1], x[0]))
                    count = len(board[r][c])
                    index = 0
                    while count > k:
                        board[r][c].remove(tmp[index][0])
                        index += 1
                        count -= 1
    ans = 0
    for r in range(n):
        for c in range(n):
            ans += len(board[r][c])
    return ans

print(solution(board, balls))
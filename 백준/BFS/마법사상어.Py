import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))
board = [[0] * N for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split(" "))
    board[r-1][c-1] = [[m, s, d]]
for _ in range(K):
    #move
    tmpBoard = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue
            for ball in board[r][c]:
                m, s, d = ball
                newr = r
                newc = c
                if d == 1:
                    newr = r - s if r-s >= 0 else N+r-s
                    newc = (c+s)%N
                if d == 2:
                    newc = (c+s)%N
                if d == 3:
                    newr = (r+s)%N
                    newc = (c+s)%N
                if d == 4:
                    newr = (r+s)%N
                if d == 5:
                    newr = (r+s)%N
                    newc = c-s if c-s >= 0 else N+c-s
                if d == 6:
                    newc = c-s if c-s >= 0 else N+c-s
                if d == 7:
                    newr = r - s if r-s >= 0 else N+r-s
                    newc = c-s if c-s >= 0 else N+c-s
                if d == 0:
                    newr = r - s if r-s >= 0 else N+r-s
                newpos = tmpBoard[newr][newc]
                if newpos == 0:
                    tmpBoard[newr][newc] = [[m,s,d]]
                else:
                    tmpBoard[newr][newc].append([m,s,d])
    board = tmpBoard
    # merge
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue
            mergeM = 0
            mergeBall = 0
            mergeV = 0
            checkd = 0
            if len(board[r][c]) == 1:
                continue
            for ball in board[r][c]:
                m, s, d = ball
                mergeM += m
                mergeBall += 1
                mergeV += s
                if d % 2 == 0:
                    checkd += 1
            tmp = []
            dtmp = [0,2,4,6] if checkd == mergeBall or checkd == 0 else [1,3,5,7]
            for newball in range(4):
                if mergeM // 5 != 0:
                    tmp.append([mergeM//5, mergeV//mergeBall, dtmp[newball]])
            board[r][c] = tmp if len(tmp) != 0 else 0
# ans
total = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            continue
        for ball in board[r][c]:
            m,s,d = ball
            total += m
print(total)
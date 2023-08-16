import sys
from itertools import combinations

input = sys.stdin.readline

N, M, H = map(int, input().split(" "))
board = [[False]*N for _ in range(H)]
for _ in range(M):
    r, c = map(int, input().split(" "))
    board[r-1][c-1] = True

def checkPutBridge(r, c, newBoard):
    if newBoard[r][c]:
        return False
    if c+1 < N and newBoard[r][c+1]:
        return False
    return True

def checkEnd(newBoard):
    for c in range(N):
        # 각 세로줄 별 체크
        r = 0
        tmpC = c
        while r < H:
            if tmpC >= N:
                break
            if tmpC < 0:
                break
            if newBoard[r][tmpC]:
                tmpC+=1
            elif newBoard[r][tmpC-1]:
                tmpC-=1
            r+=1
        if tmpC != c:
            return False
    return True

def solution():
    positons = []
    if checkEnd(board):
        return 0
    for r in range(H):
        for c in range(N-1):
            if checkPutBridge(r,c,board):
                positons.append([r,c])
    positionList = []
    for i in range(1, 4):
        positionList.extend(list(combinations(positons, i)))
    for positons in positionList:
        tmp = []
        for pos in list(positons):
            r,c = pos
            if checkPutBridge(r,c,board):
                board[r][c] = True
                tmp.append([r,c])
        if len(tmp) != len(positons):
            for pos in tmp:
                r, c = pos
                board[r][c] = False
            continue
        if checkEnd(board):
            return len(positons)
        for pos in tmp:
            r, c = pos
            board[r][c] = False
    return -1
    

print(solution())     
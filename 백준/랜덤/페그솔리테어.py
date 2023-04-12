import sys

input = sys.stdin.readline

N = int(input())
boards = []
for i in range(N):
    count = 0
    board = []
    for _ in range(5):
        board.append(list(input())[:-1])
    if i != N-1:
        input()
    boards.append(board)


dc = [-1,1,0,0]
dr = [0,0,-1,1]
minPin = 8
minMove = 1000


def isValid(r, c):
    if r < 0 or r >= 5:
        return False
    if c < 0 or c >= 9:
        return False
    return True

def dfs(start, board, pin, move):
    global minPin
    global minMove
    if pin < minPin:
        minPin = pin
        minMove = move
    elif pin == minPin and move < minMove:
        minMove = move
    for d in range(4):
        r1 = start[0] + dr[d]
        c1 = start[1] + dc[d]
        if isValid(r1,c1) and board[r1][c1] == 'o':
            r2 = r1 + dr[d]
            c2 = c1 + dc[d]
            if isValid(r2,c2) and board[r2][c2] == '.':
                board[start[0]][start[1]] = '.'
                board[r1][c1] = '.'
                board[r2][c2] = 'o'
                for r in range(5):
                    for c in range(9):
                        if board[r][c] == 'o':
                            dfs([r,c], board, pin-1, move+1)
                board[start[0]][start[1]] = 'o'
                board[r1][c1] = 'o'
                board[r2][c2] = '.'


ansList = []
for board in boards:
    maxrow = len(board)
    maxcol = len(board[0])
    initpin = 0
    for r in range(maxrow):
        for c in range(maxcol):
            if board[r][c] == 'o':
                initpin+=1
    for r in range(maxrow):
        for c in range(maxcol):
            if board[r][c] == 'o':
                dfs([r,c], board, initpin, 0)
    ansList.append([minPin, minMove])
    minPin = 8
    minMove = 1000
            
for ans in ansList:
    print(ans[0], ans[1])
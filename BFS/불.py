import sys
from collections import deque

def printBoard(board):
    for row in board:
        for item in row:
            print(item, end="")
        print("")
    print("")

def findStart(w, h, board):
    for row in range(h):
        for col in range(w):
            if (board[row][col] == "@"):
                return [row, col];

def isEnd(node,size, board):
    if node[0] == size[0] - 1 or node[0] == 0 or node[1] == size[1] - 1 or node[1] == 0:
        return True
    return False

def nodeFilter(node, board, size):
    if (node[0] < 0 or node[0] >= size[0]):
        return False
    if (node[1] < 0 or node[1] >= size[1]):
        return False  
    if (board[node[0]][node[1]] != '.'):
        return False
    return True

def getNextList(node, board, size):
    nextList = [
        [node[0] + 1, node[1]],
        [node[0] - 1, node[1]],
        [node[0], node[1] + 1],
        [node[0], node[1] - 1],
    ]
    return [x for x in nextList if nodeFilter(x, board, size)]

def spread(node, board, size, fire):
    if (node[0] < 0 or node[0] >= size[0]):
        return
    if (node[1] < 0 or node[1] >= size[1]):
        return
    if (board[node[0]][node[1]] != '#' and board[node[0]][node[1]] != '*'):
        fire.append([node[0], node[1]])
    
def fireSpread(board, size, fire):
    for _ in range(len(fire)):
        row, col = fire.popleft()
        spread([row-1, col], board, size, fire)
        spread([row+1, col], board, size, fire)
        spread([row, col-1], board, size, fire)
        spread([row, col+1], board, size, fire)
    return board

def bfs(start, size, board):
    q = deque()
    fire = deque()
    q.append(start)
    for row in range(size[0]):
        for col in range(size[1]):
            if (board[row][col] == '*'):
                fire.append([row,col])
    dist = []
    for _ in range(size[0]):
        dist.append([0]*size[1])
    dist[start[0]][start[1]] = 1
    while q:
        print(q)
        node = q.popleft()
        if (isEnd(node, size, board)):
            return dist[node[0]][node[1]]
        print(node,board[node[0]][node[1]])
        printBoard(board)
        board = fireSpread(board, size, fire)
        for next in getNextList(node, board, size):
            printBoard(board)
            print("nextList",getNextList(node, board, size))
            q.append(next)
            board[next[0]][next[1]] = 'T'
            dist[next[0]][next[1]] =  dist[node[0]][node[1]] + 1
    return 'IMPOSSIBLE'


input = sys.stdin.readline

ans = []
testCount = int(input());
for _ in range(testCount):
    w, h = list(map(int, input().split(" ")))
    board = []
    for _ in range(h):
        board.append(list(input())[0:-1])
    start = findStart(w,h,board)
    ans.append(bfs(start, [h, w], board))
for item in ans:
    print(item)



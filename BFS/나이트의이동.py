import sys
from collections import deque

def makeBoard(boardSize):
    board = []
    for _ in range(boardSize):
        row = [0] * boardSize
        board.append(row)
    return board

def checkPosition(x, y, boardSize):
    if (x < 0 or y < 0):
        return False
    if (x >= boardSize or y >= boardSize):
        return False
    return True

def nextList(node, boardSize):
    nextList = [
        [node[0] - 2, node[1] + 1],
        [node[0] - 1, node[1] + 2],
        [node[0] + 1, node[1] + 2],
        [node[0] + 2, node[1] + 1],
        [node[0] + 2, node[1] - 1],
        [node[0] + 1, node[1] - 2],
        [node[0] - 1, node[1] - 2],
        [node[0] - 2, node[1] - 1],
    ]
    return [x for x in nextList if checkPosition(x[0], x[1], boardSize)]

def bfs(boardSize, start, end):
    q = deque()
    q.append(start)
    board = makeBoard(boardSize)
    while q:
        node = q.popleft()
        if (node == end):
            return board[node[0]][node[1]]
        for next in nextList(node, boardSize):
            if not board[next[0]][next[1]]:
                q.append(next)
                board[next[0]][next[1]] = board[node[0]][node[1]] + 1


totalTest = int(sys.stdin.readline())
ans = []
for i in range(totalTest):
    boardSize = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split(" ")))
    end = list(map(int, sys.stdin.readline().split(" ")))
    ans.append(bfs(boardSize, start, end))

for item in ans:
    print(item)
import sys
from collections import deque

input = sys.stdin.readline

def checkNextNode(next):
    if (next[0] < 0):
        return False
    if (next[0] >= N):
        return False
    if (next[1] < 0):
        return False
    if (next[1] >= M):
        return False
    return True

def getNextNodeList(node):
    nextList = []
    if checkNextNode([node[0]-1, node[1]]):
        nextList.append([node[0]-1, node[1]])
    if checkNextNode([node[0]+1, node[1]]):
        nextList.append([node[0]+1, node[1]])
    if checkNextNode([node[0], node[1]-1]):
        nextList.append([node[0], node[1]-1])
    if checkNextNode([node[0], node[1]+1]):
        nextList.append([node[0], node[1]+1])
    return nextList

def sameWithStartBlind(startColor, current):
    if (startColor == 'R' or startColor == 'G'):
        if (current == 'B'):
            return False
        else:
            return True
    else:
        if (current == 'B'):
            return True
        else:
            return False
def sameWithStart(startColor, current):
    if (startColor == current):
        return True
    else:
        return False

def bfs(start, colorBoard, checkColor):
    startColor = colorBoard[start[0]][start[1]]
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if colorBoard[node[0]][node[1]] == '0':
            continue
        colorBoard[node[0]][node[1]] = '0'
        for next in getNextNodeList(node):
            if checkColor(startColor, colorBoard[next[0]][next[1]]):
                q.append(next)


N = int(input())
boardOne = []
boardTwo = []
for _ in range(N):
    row = list(input())
    row.pop()
    boardOne.append(row)
    newRow = row[:]
    boardTwo.append(newRow)
M = len(row)
ans = [0,0]
func = [sameWithStart, sameWithStartBlind]
boards = [boardOne, boardTwo]
for i in range(2):
    for rowIdx in range(N):
        for colIdx in range(M):
            if (boards[i][rowIdx][colIdx] != '0'):
                bfs([rowIdx, colIdx],boards[i], func[i])
                ans[i]+=1
print(' '.join(map(str, ans)))
            
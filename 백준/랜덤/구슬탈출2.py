import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(input())[:-1])

R = []
B = []
O = []
q = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            R.append(r)
            R.append(c)
        if board[r][c] == "B":
            B.append(r)
            B.append(c)
        if board[r][c] == "O":
            O.append(r)
            O.append(c)

def getWayPos(way, node):
    if way == "r":
        return [node[0], node[1]+1, 'r']
    if way == "l":
        return [node[0], node[1]-1, 'l']
    if way == "u":
        return [node[0]-1, node[1], 'u']
    if way == "d":
        return [node[0]+1, node[1], 'd']

def checkTogo(way, node, color):
    check = 'B' if color == "R" else 'R'
    nextPos = getWayPos(way, node)
    if board[nextPos[0]][nextPos[1]] == "." or board[nextPos[0]][nextPos[1]] == "O":
        return True
    twoNext = getWayPos(way, nextPos)
    if board[nextPos[0]][nextPos[1]] == check and board[twoNext[0]][twoNext[1]] != "#":
        return True
    return False

def moveBall(way, node, endFlag, dist):
    global B
    board[node[0]][node[1]] = '.'
    prev = [node[0], node[1]]
    while checkTogo(way, node, 'R'):
        if board[node[0]][node[1]] == "O":
            endFlag = True
        node = getWayPos(way, node)
    if board[node[0]][node[1]] == "O":
        endFlag = True
    board[node[0]][node[1]] = 'R'
    dist[node[0]][node[1]] = dist[prev[0]][prev[1]] + 1
    if node[2] != 'l' and checkTogo('r', node, 'R'):
        q.append([node[0], node[1], 'r'])
    if node[2] != 'r' and checkTogo('l', node, 'R'):
        q.append([node[0], node[1], 'l'])
    if node[2] != 'd' and checkTogo('u', node, 'R'):
        q.append([node[0], node[1], 'u'])
    if node[2] != 'u' and checkTogo('d', node, 'R'):
        q.append([node[0], node[1], 'd'])

    # 파란볼 옮겨주기
    board[B[0]][B[1]] = '.'
    while checkTogo(way, B, 'B'):
        if board[B[0]][B[1]] == "O":
            endFlag = False
        B = getWayPos(way,B)
    if board[B[0]][B[1]] == "O":
        endFlag = False
    board[B[0]][B[1]] = 'B'
    return endFlag


if checkTogo('r', R, 'R'):
    q.append([R[0], R[1], 'r'])
if checkTogo('l', R, 'R'):
    q.append([R[0], R[1], 'l'])
if checkTogo('u', R, 'R'):
    q.append([R[0], R[1], 'u'])
if checkTogo('d', R, 'R'):
    q.append([R[0], R[1], 'd'])
endFlag = False
dist = [[0] * M for _ in range(N)]
dist[R[0]][R[1]] = 1
start = True
while q:
    node = q.pop()
    if node[2] == 'r':
        endFlag = moveBall('r', node, endFlag, dist)
    if node[2] == 'l':
        endFlag = moveBall('l', node, endFlag, dist)
    if node[2] == 'u':
        endFlag = moveBall('u', node, endFlag, dist)
    if node[2] == 'd':
        endFlag = moveBall('d', node, endFlag, dist)
    if endFlag:
        print(dist[node[0]][node[1]])
        break
    if not start and node[0] == R[0] and node[1] == R[1]:
        break
    start = False
if not endFlag:
    print(-1)
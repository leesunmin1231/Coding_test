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
        

def bfs(start):
    q = deque();
    q.append(start) # 시작 노드 넣기
    while q:
        node = q.popleft()
        if (board[node[0]][node[1]] == 0):
            continue
        board[node[0]][node[1]] = 0 # 방문한 노드
        for next in getNextNodeList(node):
            if board[next[0]][next[1]] == 1:
                q.append(next)


T = int(input())
ans = []
for _ in range(T):
    M, N, K = map(int, input().split(" "))
    board = []
    for _ in range(N):
        tmp = [0]*M
        board.append(tmp)
    for _ in range(K):
        X, Y = map(int, input().split(" "))
        board[Y][X] = 1
    count = 0
    for rowIdx in range(N):
        for colIdx in range(M):
            if (board[rowIdx][colIdx]):
                bfs([rowIdx, colIdx])
                count+=1
    ans.append(count)
for i in range(T):
    print(ans[i])

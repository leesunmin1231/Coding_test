import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def getMax(node):
    num = 0
    for row in node:
        n = max(row)
        if n > num:
            num = n
    return num

def checkMoveOver(node, prev):
    for i in range(N):
        if node[i] != prev[i]:
            return False
    return True

def getNextList(node):
    result = []
    # 상
    copynode = copy.deepcopy(node)
    for j in range(N):
        p = 0

        for i in range(1, N):
            if copynode[i][j]:
                temp = copynode[i][j]
                copynode[i][j] = 0

                if copynode[p][j] == 0:
                    copynode[p][j] = temp

                elif copynode[p][j] == temp:
                    copynode[p][j] *= 2
                    p += 1

                else:
                    p += 1
                    copynode[p][j] = temp
    result.append(copynode)
     # 하
    copynode = copy.deepcopy(node)
    for j in range(N):
        p = N - 1

        for i in range(N - 2, -1, -1):
            if copynode[i][j]:
                temp = copynode[i][j]
                copynode[i][j] = 0

                if copynode[p][j] == 0:
                    copynode[p][j] = temp
                elif copynode[p][j] == temp:
                    copynode[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    copynode[p][j] = temp

    result.append(copynode)
     # 좌
    copynode = copy.deepcopy(node)
    for i in range(N):
        p = 0

        for j in range(1, N):
            if copynode[i][j]:
                temp = copynode[i][j]
                copynode[i][j] = 0

                if copynode[i][p] == 0:
                    copynode[i][p] = temp
                elif copynode[i][p] == temp:
                    copynode[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    copynode[i][p] = temp
    result.append(copynode)
     # 우
    copynode = copy.deepcopy(node)
    for i in range(N):
        p = N - 1

        for j in range(N - 2, -1, -1):
            if copynode[i][j]:
                temp = copynode[i][j]
                copynode[i][j] = 0

                if copynode[i][p] == 0:
                    copynode[i][p] = temp
                elif copynode[i][p] == temp:
                    copynode[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    copynode[i][p] = temp
    result.append(copynode)
    return result

q = deque()
q.append([board, 0])
result = []
while q:
    node, count = q.popleft()
    if count > 4:
        result.append(getMax(node))
        continue
    for next in getNextList(node):
        q.append([next, count + 1])

print(max(result))
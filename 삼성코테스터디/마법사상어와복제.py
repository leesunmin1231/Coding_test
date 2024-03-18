import sys
import copy
from collections import deque


input = sys.stdin.readline

def mergeFishSmell(fishSmellQ):
    first = fishSmellQ[0]
    second = fishSmellQ[1]
    fishSmell = [[False] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if first[r][c] or second[r][c]:
                fishSmell[r][c] = True
    return fishSmell

def moveFish(board, fishSmell, shark):
    # 1, 2, 3, 4, 5, 6, 7, 8
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    newBoard = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if len(board[r][c]) == 0: 
                continue
            for d in board[r][c]:
                nextr = r
                nextc = c
                nextd = d
                for i in range(8):
                    nr = r + dr[(d-i) % 8]
                    nc = c + dc[(d-i) % 8]
                    if nr < 0 or nr >= 4:
                        continue
                    if nc < 0 or nc >= 4:
                        continue
                    if fishSmell[nr][nc]:
                        continue
                    if nr == shark[0] and nc == shark[1]:
                        continue
                    nextr = nr
                    nextc = nc
                    nextd = (d-i) % 8
                    break
                newBoard[nextr][nextc].append(nextd)
    return newBoard
                
def moveShark(board, shark):
    q = deque()
    q.append([shark[0], shark[1], 0, '' , 0, []])
    totalFish = 0
    result = [shark[0], shark[1]]
    deleteFishList = []
    sharkDir = '999'
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    while q:
        r, c, count, dir, checkFish, tmpList = q.popleft()
        if count == 3:
            if len(board[r][c]) != 0:
                tmpList.append([r,c])
            if totalFish < checkFish:
                result = [r,c]
                deleteFishList = tmpList
                totalFish = checkFish
                sharkDir=dir
                continue
            if checkFish == totalFish and int(sharkDir) > int(dir):
                sharkDir = dir
                result = [r,c]
                deleteFishList = tmpList
                continue
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= 4:
                continue
            if nc < 0 or nc >= 4:
                continue
            tmp = copy.deepcopy(tmpList)
            newCheck = checkFish+len(board[nr][nc])
            if [nr,nc] in tmp:
                newCheck = checkFish
            if len(board[nr][nc]) != 0:
                tmp.append([nr,nc])
            q.append([nr, nc, count+1, dir + str(i+1), newCheck, tmp])
    return result, deleteFishList

def deleteFish(board, deleteFishList):
    newFishSmell = [[False] * 4 for _ in range(4)]
    for node in deleteFishList:
        r, c = node
        board[r][c] = []
        newFishSmell[r][c] = True
    return board, newFishSmell

def copyComplete(board, copyBoard):
    for r in range(4):
        for c in range(4):
            board[r][c].extend(copyBoard[r][c])
    return board

board = [[[] for _ in range(4)] for _ in range(4)]
M, S = map(int, input().split(" "))
fishes = []
for _ in range(M):
    fx, fy, d = map(int, input().split(" "))
    fishes.append([fx-1, fy-1, d-1])
    board[fx-1][fy-1].append(d-1)
sx, sy = map(int, input().split(" "))
shark = [sx-1, sy-1]

fishSmellQ = deque()
fishSmellQ.append([[False] * 4 for _ in range(4)])
fishSmellQ.append([[False] * 4 for _ in range(4)])

count = 0
while count < S:
    # 현재 물고기들 위치 새로운 배열에 복제해두기
    copyBoard = copy.deepcopy(board)
    fishSmell = mergeFishSmell(fishSmellQ)
    # 물고기 이동
    board = moveFish(board, fishSmell, shark)
    # 상어 이동
    shark, deleteFishList = moveShark(board, shark)
    # 상어가 있는 자리 모든 물고기 제거, 새로운 물고기 냄새
    board, newFishSmell = deleteFish(board, deleteFishList)
    # 두번전 물고기 냄새 사라짐
    fishSmellQ.popleft()
    fishSmellQ.append(newFishSmell)
    # 복제 마법 완료
    board = copyComplete(board, copyBoard)
    count+=1

ans = 0
for r in range(4):
    for c in range(4):
        ans += len(board[r][c])
print(ans)
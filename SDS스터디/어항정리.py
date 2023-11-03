import sys

input = sys.stdin.readline

n, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

def checkEnd(arr):
    return max(arr) - min(arr)

def putFish(arr):
    minNum = min(arr)
    for i in range(n):
        if arr[i] == minNum:
            arr[i] += 1

def getBlockRotate90(rotateBlock, restArr):
    colLength = len(rotateBlock)
    newRestArr = restArr[colLength:]
    rotate = [[row[i] for row in rotateBlock[::-1]] for i in range(len(rotateBlock[0]))]
    newRotateBlock = rotate + [restArr[:colLength]]
    return [newRotateBlock, newRestArr]

def calculateFish(rotateBlock, restArr):
    newRotateBlock = [row[:] for row in rotateBlock[:]]
    newRestArr = restArr[:]
    for r in range(len(rotateBlock)):
        for c in range(len(rotateBlock[0])-1):
            one = rotateBlock[r][c]
            two = rotateBlock[r][c+1]
            d = abs(one-two) // 5
            if d > 0:
                if one > two:
                    newRotateBlock[r][c] -= d
                    newRotateBlock[r][c+1] += d
                else:
                    newRotateBlock[r][c] += d
                    newRotateBlock[r][c+1] -= d
    for r in range(len(rotateBlock)-1):
        for c in range(len(rotateBlock[0])):
            one = rotateBlock[r][c]
            two = rotateBlock[r+1][c]
            d = abs(one-two) // 5
            if d > 0:
                if one > two:
                    newRotateBlock[r][c] -= d
                    newRotateBlock[r+1][c] += d
                else:
                    newRotateBlock[r][c] += d
                    newRotateBlock[r+1][c] -= d
    if len(restArr) != 0:
        for i in range(len(restArr)-1):
            one = restArr[i]
            two = restArr[i+1]
            d = abs(one-two) // 5
            if d > 0:
                if one > two:
                    newRestArr[i] -= d
                    newRestArr[i+1] += d
                else:
                    newRestArr[i] += d
                    newRestArr[i+1] -= d
        one = rotateBlock[len(rotateBlock)-1][len(rotateBlock[0])-1]
        two = restArr[0]
        d = abs(one-two) // 5
        if d > 0:
            if one > two:
                newRotateBlock[len(rotateBlock)-1][len(rotateBlock[0])-1] -= d
                newRestArr[0] += d
            else:
                newRotateBlock[len(rotateBlock)-1][len(rotateBlock[0])-1] += d
                newRestArr[0] -= d
    return newRotateBlock, newRestArr

def changeToLine(rotateBlock, restArr):
    newArr = []
    tmp = [[row[i] for row in rotateBlock[::-1]] for i in range(len(rotateBlock[0]))]
    for row in tmp:
        newArr += row[:]
    newArr += restArr[:]
    return newArr

def getBlockRotate180(rotate, rest):
    tmp = [[row[i] for row in rotate[::-1]] for i in range(len(rotate[0]))]
    rotated = [[row[i] for row in tmp[::-1]] for i in range(len(tmp[0]))]
    return rotated + rest


ans = 0
while True:
    # 물고기 가장 많이 들어있는 수 - 가장 적게 들어있는 수 반환
    count = checkEnd(arr)
    if count <= k:
        print(ans)
        break
    ans += 1

    # 물고기 수가 적은 어항에 한마리씩 넣기
    putFish(arr)

    # 어항 한개 쌓기
    # 2개 이상 쌓인 어항 시계방향 90도 회전후 쌓기 반복 => 못쌓을 때까지
    rotateBlock = [[arr[0]]]
    restArr = arr[1:]
    while True:
        if len(rotateBlock) > len(restArr):
            break
        rotateBlock, restArr = getBlockRotate90(rotateBlock, restArr)


    # 인접한 물고기 수 차이를 5로 나눈 몫 d, d가 0보다 크면 물고기 많은 곳은 - d, 물고기 적은 곳은 +d
    rotateBlock, restArr = calculateFish(rotateBlock, restArr)

    # 어항 일렬로 놓기. 왼쪽 아래 -> 오른쪽 위
    arr = changeToLine(rotateBlock, restArr)

    # 공중 부양 n/2개를 180도 회전후 위에 놓기
    block = getBlockRotate180([arr[:n//2]], [arr[n//2:]])
    # 다시 n/4를 180도 회전후 위에 놓기
    rotateBlock = []
    restBlock = []
    for row in block:
        rotateBlock.append(row[:n//4])
        restBlock.append(row[n//4:])
    block = getBlockRotate180(rotateBlock, restBlock)
    # 인접한 물고기 수 차이를 5로 나눈 몫 d, d가 0보다 크면 물고기 많은 곳은 - d, 물고기 적은 곳은 +d
    block, tmp = calculateFish(block, [])
    # 어항 일렬로 놓기. 왼쪽 아래 -> 오른쪽 위
    arr = changeToLine(block, [])

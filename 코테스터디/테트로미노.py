import sys

input = sys.stdin.readline

tetroList = [
    # 1자
    [[0,0], [0,1], [0,2], [0,3]],
    [[0,0], [1,0], [2,0], [3,0]],
    # 네모
    [[0,0], [0,1], [1,0], [1,1]],
    # L 자
    [[0,0], [1,0], [2,0], [2,1]],
    [[0,0], [0,1], [-1,1], [-2,1]],
    [[0,0], [0,1], [0,2], [-1,2]],
    [[0,0], [1,0], [1,1], [1,2]],
    [[0,0], [0,1], [1,1], [2,1]],
    [[0,0], [1,0], [0,1], [0,2]],
    [[0,0], [0,1], [1,0], [2,0]],
    [[0,0], [0,1], [0,2], [1,2]],
    # 계단
    [[0,0], [1,0], [1,1], [2,1]],
    [[0,0], [0,1], [-1,1], [1,0]],
    [[0,0], [0,1], [-1,1], [-1,2]],
    [[0,0], [0,1], [1,1], [1,2]],
    # ㅗ
    [[0,0], [-1,0], [0,-1], [0,1]],
    [[0,0], [1,0], [0,-1], [0,1]],
    [[0,0], [-1,0], [1,0], [0,1]],
    [[0,0], [-1,0], [1,0], [0,-1]]
]

n, m = map(int, input().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, input().split(" "))))

def getTotal(r,c, tetro):
    result = 0
    for dr,dc in tetro:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= n:
            return 0
        if nc < 0 or nc >= m:
            return 0
        result += board[nr][nc]
    return result

result = 0
for tetro in tetroList:
    for r in range(n):
        for c in range(m):
            num = getTotal(r,c,tetro)
            if result < num:
                result = num
print(result)
            

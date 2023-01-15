# 신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다. 각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다. 창영이는 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.

# 궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다. 방향이 다른 돌상은 깨달음에 치명적이다. 깨달음의 양은 아래와 같이 정의된다.

# | (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |

# 창영이는 궁극의 깨달음을 얻을 수 있을까?



import sys

N = int(sys.stdin.readline().rstrip())
dirList = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = 0
maxNum = 0

for start in range(N):
    tmp = 0
    for index in range(start, N):
        if (dirList[index] == 1):
            left+=1
        else:
            right+=1
        if abs(left-right) > tmp:
            tmp = abs(left-right)
    if (tmp > maxNum):
        maxNum = tmp

print(maxNum)
import sys
input = sys.stdin.readline

N = int(input())
check = 0
num = 666
while True:
    tofind = str(num).find('666')
    if tofind != -1:
        check+=1
    if check == N:
        break
    num+=1
print(num)
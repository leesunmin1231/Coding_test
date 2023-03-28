import sys
def check666(num):
    if ("666" in num):
        return True
    return False

totalCount = int(sys.stdin.readline().rstrip())
count = 0
answer = 666
i = 666
while(True):
    if (check666(str(i))):
        count+=1
    if (count == totalCount):
        answer = i
        break
    i+=1
print(answer)

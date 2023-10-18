import sys

input = sys.stdin.readline

def checkSen(sen):
    stack = []
    for i in list(sen):
        if i == "(":
            stack.append(i)
        elif i == "[":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            prev = stack.pop()
            if prev != "(":
                return False
        elif i == "]":
            if not stack:
                return False
            prev = stack.pop()
            if prev != "[":
                return False
    if stack:
        return False
    return True

arr = []

while True:
    sen = input().replace("\n", "")
    if sen == ".":
        break
    if checkSen(sen):
        arr.append("yes")
    else:
        arr.append("no")

for ans in arr:
    print(ans)
import sys

input = sys.stdin.readline

line = input()
arr = []
num = ""
for i in range(len(line)):
    if line[i].isdigit():
        num += line[i]
    else:
        arr.append(int(num))
        arr.append(line[i])
        num = ""
arr.pop()
tmp = []
i = 0
sumNum = arr[0]
while i < len(arr):
    if arr[i] == "-":
        tmp.append(sumNum)
        tmp.append(arr[i])
        sumNum = arr[i+1]
    elif arr[i] == "+":
        sumNum += arr[i+1]
    i+=1
tmp.append(sumNum)
ans = tmp[0]
for a in range(len(tmp)):
    if tmp[a] == "-":
        ans -= tmp[a+1]
print(ans)
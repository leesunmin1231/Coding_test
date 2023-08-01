import sys

input = sys.stdin.readline

arr = list(input())[:-1]
countB = 0
for b in arr:
    if b == "b":
        countB+=1

start = 0
end = countB-1
countA = 0
for i in range(start, end+1):
    if arr[i] == "a":
        countA+=1
tmp = countA
while end < len(arr)-1:
    if arr[start] == "a":
        tmp-=1
    if arr[end+1] == "a":
        tmp += 1
    if tmp < countA:
        countA = tmp
    start+=1
    end+=1
end = 0
while start < len(arr)-1:
    if arr[start] == "a":
        tmp -= 1
    if arr[end] == "a":
        tmp += 1
    if tmp < countA:
        countA = tmp
    start+=1
    end+=1
print(countA)
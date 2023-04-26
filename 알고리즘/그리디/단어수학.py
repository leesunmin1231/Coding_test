import sys
input = sys.stdin.readline

N = int(input())
arr = []
maxLen = 0
for _ in range(N):
    tmp = list(input())[:-1]
    arr.append(tmp)
    if len(tmp) > maxLen:
        maxLen = len(tmp)
dic = {}
n = 9
for i in range(maxLen,-1,-1):
    for word in arr:
        if len(word) <= i:
            continue
        if word[len(word) - i-1] not in dic:
            dic[word[len(word) - i-1]] = n
            n -= 1
result = []
for word in arr:
    tmp = ""
    for n in word:
        tmp += str(dic[n])
    result.append(int(tmp))
print(sum(result))
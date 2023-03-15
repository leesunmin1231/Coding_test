import sys
input = sys.stdin.readline


n = int(input())

d = [0, []] * (n+1)
d[2] = [1, [1,2]]
d[1] = [0, [1]]
for i in range(3, n+1):
    if i % 3 == 0 and i % 2 == 0:
        minCount = min([d[i//3], d[i//2], d[i-1]], key= lambda x:x[0])
    elif i % 3 == 0:
        minCount = min([d[i//3], d[i-1]], key= lambda x:x[0])
    elif i % 2 == 0:
        minCount = min([d[i//2], d[i-1]], key= lambda x:x[0])
    else:
        minCount = d[i-1]
    d[i] = [minCount[0]+1, minCount[1] + [i]]
print(d[n][0])
d[n][1].reverse()
print(' '.join(map(str, d[n][1])))
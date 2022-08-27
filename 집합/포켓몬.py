import sys
nm = list(map(int, input().split(" ")))
dic = {}
for i in range(nm[0]):
    line = sys.stdin.readline().strip()
    dic[i+1] = line
    dic[line] = i+1

for i in range(nm[1]):
    line = sys.stdin.readline().strip()
    if line.isdigit():
        print(dic[int(line)])
    else:
        print(dic[line])
import sys
nm = list(map(int, input().split(" ")))
lst = []
for i in range(nm[0]):
    line = sys.stdin.readline().strip()
    lst.append(line)

for i in range(nm[1]):
    line = sys.stdin.readline().strip()
    if line.isdigit():
        print(lst[int(line)-1])
    else:
        print(lst.index(line)+1)
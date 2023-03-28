def hanoi(N, start, middle, dest):
    if N == 1:
        lst.append((start, dest))
        return
    hanoi(N-1, start, dest, middle)
    hanoi(1, start, middle, dest)
    hanoi(N-1, middle, start, dest)

lst = []
num = int(input())
hanoi(num, 1, 2, 3)
print(len(lst))
for i in lst:
    print(i[0], i[1])
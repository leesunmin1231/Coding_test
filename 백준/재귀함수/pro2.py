lst=[]
def hanoi (num, start, by, end):
    if (num == 1):
        lst.append((start, end))
    else:
        hanoi(num-1, start, end, by)
        lst.append((start, end))
        hanoi(num-1, by, start, end)

num = int(input(""))
hanoi(num,1,2,3)
print(len(lst))
for i in lst:
    print(i[0] , i[1])        
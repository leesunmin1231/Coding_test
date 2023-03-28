def recur(n, lst):
    if n == 1:
        for i in lst:
            print(i)
        return
    new_lst = []
    for j in range(len(lst)):
        first_line = ""
        for i in range(3):
            first_line += lst[j]
        new_lst.append(first_line)
    for i in range(len(lst)):
        second_line = ""
        for j in range(3):
            if j == 1:
                second_line+=' '*len(lst[0])
            else:
                second_line+=lst[i]
        new_lst.append(second_line)
    for j in range(len(lst)):
        third_line = ""
        for i in range(3):
            third_line += lst[j]
        new_lst.append(third_line)
    recur(n//3, new_lst)

lst = ['*']
num = int(input())
recur(num,lst)
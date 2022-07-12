def solution(str1, str2):
    lst1 = []
    lst2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        if not str1[i].isalpha():
            continue
        if not str1[i+1].isalpha():
            continue
        lst1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if not str2[i].isalpha():
            continue
        if not str2[i+1].isalpha():
            continue
        lst2.append(str2[i:i+2])
    inter = []
    tmp = []
    for item in lst1:
        if item in tmp:
            continue
        f_count = lst1.count(item)
        if item in lst2:
            s_count = lst2.count(item)
            if f_count > s_count:
                for i in range(s_count):
                    inter.append(item)
            else:
                for i in range(f_count):
                    inter.append(item)
        tmp.append(item)

    if len(lst1) + len(lst2) - len(inter) == 0:
        return 65536
    answer = int((len(inter)/(len(lst1) + len(lst2) - len(inter))) * 65536)
    return answer

print(solution("FRANCE","french"))

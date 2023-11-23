def solution(n, k, cmd):
    linkedList = {} # index: [prevIndex, nextIndex]
    deleteArr = [False] * n
    for i in range(n):
        linkedList[i] = [i-1, i+1]
    linkedList[0][0] = None
    linkedList[n-1][1] = None
    stack = []
    cursor = k
    for line in cmd:
        line = line.split(" ")
        if line[0] == "U":
            term = int(line[1])
            while term > 0:
                term -= 1
                cursor = linkedList[cursor][0]
        elif line[0] == "D":
            term = int(line[1])
            while term > 0:
                term -= 1
                cursor = linkedList[cursor][1]
        elif line[0] == "C":
            stack.append([cursor] + linkedList[cursor])
            prev, next = linkedList[cursor]
            if prev != None:
                linkedList[prev][1] = next
            if next != None:
                linkedList[next][0] = prev
            deleteArr[cursor] = True
            cursor = next
            if not cursor:
                cursor = prev
        elif line[0] == "Z":
            current, prev, next = stack.pop()
            if prev != None:
                linkedList[prev][1] = current
            if next != None:
                linkedList[next][0] = current
            linkedList[current] = [prev, next]
            deleteArr[current] = False
            
    ans = ""
    for flag in deleteArr:
        if flag:
            ans += "X"
        else:
            ans += "O"
    return ans
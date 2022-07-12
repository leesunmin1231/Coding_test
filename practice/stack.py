# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
#   만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class ArrayStack:
    def __init__(self):
        self.StackArr = []
    def Push(self, x):
        self.StackArr.append(x)
    def Pop(self):
        try:
            return self.StackArr.pop()
        except IndexError:
            return -1
    def Size(self):
        return len(self.StackArr)
    def Empty(self):
        if len(self.StackArr) == 0:
            return 1
        else:
            return 0
    def Top(self):
        try:
            return self.StackArr[-1]
        except IndexError:
            return -1

import sys

count = int(sys.stdin.readline())
S = ArrayStack()
for i in range (count):
    op = sys.stdin.readline().strip().split()
    if len(op) == 2:
        S.Push(op[1])
    else:
        if op[0] == "pop":
            print(S.Pop())
        elif op[0] == "size":
            print(S.Size())
        elif op[0] == "empty":
            print(S.Empty())
        else:
            print(S.Top())
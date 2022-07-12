class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):   # 스택 요소 삭제 pop()
        return self.items.pop()
    def peek(self):  # 스택 맨 앞 요소 리턴
        return self.items[0]
    def isEmpty(self):  # 스택이 비었는지 확인(비었으면 True 리턴)
        return not self.items
    
 
stk = stack()        # stack 객체 생성
print(stk)           # stack object 생성 확인
# => <__main__.stack object at 0x000001915CB04470> : 생성됨
print(stk.isEmpty()) # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)          # stk 에 1 넣음 : [1]
stk.push(2)          # stk 에 2 넣음 : [1,2]
print(stk.items)     # =>  [1,2]
print(stk.pop())     # stk 에 2가 꺼내지면서 출력 : 2 / [1]
print(stk.peek())    # stk 맨 앞 값 출력 : 1
print(stk.isEmpty()) # 비어있지 않으므로 False 출력
print(stk.pop())     # stk 에 1가 꺼내지면서 출력 : 1 / []
print(stk.isEmpty()) # 객체에 아무것도 들어있지 않으므로 True 출력
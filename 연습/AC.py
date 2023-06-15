from collections import deque
import sys
T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip() #p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
    n = int(sys.stdin.readline())
    array_list = deque(sys.stdin.readline().rstrip()[1:-1].split(","))#[x1,...,xn]과 같은 형태로 배열에 들어있는 정수
    #값이 0 일 때 예외 처리
    if '' in array_list:
        array_list.pop()
    
    reverse_flag = 0
    error_flag = 0

    for cmd in p:
        if cmd == "R":
           reverse_flag += 1
            # print("R, 뒤집은 후",array_list)
        else:#D 일 때
            #배열이 비어있는 경우
            if len(array_list) < 1:
                error_flag = 1
                break
            else:
                if reverse_flag % 2 == 0:
                    array_list.popleft()
                else:
                    array_list.pop()
                
    #출력
    if error_flag == 1:
        print("error")
    else:
        if reverse_flag % 2 == 0:
            print("["+",".join(array_list)+"]")
        else:
            array_list.reverse()
            print("["+",".join(array_list)+"]")
import sys

input = sys.stdin.readline

init = list(input().strip())
n = len(init)
m = int(input())

st1 = []
st2 = []

for i in init:
    st1.append(i)

for _ in range(m):
    cmd = input().strip()
    if cmd[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif cmd[0] == "B":
        if st1:
            st1.pop()
    else:
        st1.append(cmd[2])
st2.reverse()
print(*st1, sep="", end="")
print(*st2, sep="")
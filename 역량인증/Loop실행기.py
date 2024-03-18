import sys

def input_data():
	readl = sys.stdin.readline
	loop = readl().strip()
	return loop



# 입력 받는 부분
loop = input_data()
stack = []

# 코드를 작성하세요
i = 0
while i < len(loop):
	if loop[i] == ">":
		target = stack.pop()
		tmp = []
		while target != "<":
			tmp.append(target)
			target = stack.pop()
		count = int(tmp.pop())
		tmp.reverse()
		for _ in range(count):
			stack.extend(tmp)
	else:
		stack.append(loop[i])
	i += 1
print(''.join(stack))
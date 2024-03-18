import sys
import string

def InputData():
	readl = sys.stdin.readline
	B, S, D = readl().strip().split()
	return int(B), S, D
# 입력

arr = []

for i in range(10):
	arr.append(str(i))
arr.extend(list(string.ascii_uppercase))
	

def convertToDecimal(B, num):
	result = 0
	minus = False
	if num[0] == "-":
		minus = True
		num = num[1:]
	length = len(num) - 1
	for target in num:
		idx = arr.index(target)
		result += idx * B ** length
		length -= 1
	if minus:
		return -1 * result
	return result

def convertToBase(B, num):
	result = ""
	if num == 0:
		return "0"
	minus = False
	if num < 0:
		minus = True
		num *= -1
	while num > 0:
		r = num % B
		num = num // B
		result += arr[r]
	if minus:
		return "-"+result[::-1]
	return result[::-1]

# N : 테스트 케이스 수
# B : 진법
# S : 첫 번째 정수
# D : 두 번째 정수
N = int(input())
for _ in range(N):
	B, S, D = InputData()
	ans = -1
	# 코드를 작성 하세요
	print(convertToBase(B, convertToDecimal(B, S) * convertToDecimal(B, D)))


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	cnt_box = list(map(int, readl().split()))
	return N, cnt_box


sol = 0
sol_box_cnt = []

# 입력받는 부분
N, cnt_box = input_data()
boxes = [1, 5, 10, 50, 100, 500, 1000, 3000, 6000, 12000]


def find_next_box(cur):
	next_box = cur + 1
	while cnt_box[next_box] == 0:
		next_box += 1
	return next_box

# 여기서부터 작성
for i in range(len(boxes)-1):
	if N == 0:
		sol_box_cnt.append(0)
		continue
	nextBox = find_next_box(i)
	rest_product = N % boxes[nextBox]
	rest_box = rest_product // boxes[i]
	N -= rest_product
	
	more_box = ((cnt_box[i] - rest_box) // (boxes[nextBox] // boxes[i])) * (boxes[nextBox] // boxes[i])
	more_product = more_box * boxes[i]
	if N - more_product < 0:
		more_product = N
		more_box = more_product // boxes[i]
	N -= more_product
	total_box = more_box + rest_box
	sol_box_cnt.append(total_box)

sol_box_cnt.append(N // boxes[-1])
	
print(sum(sol_box_cnt))
print(' '.join(map(str, sol_box_cnt)))
original = [[1, 2, 3], [4, 5, 6]]
rotate = [[row[i] for row in original] for i in range(len(original[0])-1,-1,-1)]
for row in original:
    print(row)
print("")
for row in rotate:
    print(row)



[[row[i] for row in original] for i in range(len(original[0])-1,-1,-1)]
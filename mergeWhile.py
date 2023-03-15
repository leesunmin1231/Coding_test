def merge(left, right):
    sortedArr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedArr.append(left[i])
            i+=1
        else:
            sortedArr.append(right[j])
            j+=1
    while i < len(left):
        sortedArr.append(left[i])
        i+=1
    while j < len(right):
        sortedArr.append(right[j])
        j+=1
    return sortedArr

def merge_sort(arr):
    stack = []
    stack.append(len(arr)//2)
    sortedArr = []
    while len(stack) != 0:
        mid = stack.pop()
        left =arr[:mid]
        right = arr[mid:]
        if len(left) <= 1:
            continue
        sortedArr = merge(left, right)
        stack.append(len(left))
        stack.append(len(right))
        
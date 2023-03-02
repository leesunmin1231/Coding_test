def merge(left, right):
    i, j = 0,0
    sortedArr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedArr.append(left[i])
            i += 1
        else:
            sortedArr.append(right[j])
            j += 1
    while i < len(left):
        sortedArr.append(left[i])
    while j < len(right):
        sortedArr.append(right[j])
    return sortedArr

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
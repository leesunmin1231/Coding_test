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
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

arr = [3,4,1,2]
print(merge_sort(arr))
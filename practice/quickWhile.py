def partition(arr, start, end):
    pivot = arr[start]
    i = start
    for j in range(start + 1, end + 1):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
    arr[start] = arr[i]
    arr[i] = pivot
    return i

def quick(arr):
    stack = []
    stack.append((0, len(arr)-1))
    while len(stack) !=0:
        start, end = stack.pop()
        q = partition(arr, start, end)
        if start >= end:
            continue
        stack.append((start, q))
        stack.append((q+1, end))



arr = [3,4,1,2,6,7,5]
quick(arr)
print(arr)
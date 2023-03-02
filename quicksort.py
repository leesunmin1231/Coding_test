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

def quick(arr, start, end):
    if start >= end:
        return
    q = partition(arr, start, end)
    print(arr[q], arr)
    quick(arr, start, q)
    quick(arr, q + 1, end)

arr = [3,4,1,2,6,7,5]
quick(arr,0,6)
print(arr)
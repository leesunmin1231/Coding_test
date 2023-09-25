arr = [1,2,3,4,5,6,7,8]

def binarySearch(arr, data, start, end):
    pivot = (start+end) // 2
    if arr[pivot] == data:
        return pivot
    if arr[pivot] < data:
        return binarySearch(arr, data, pivot+1, end)
    else:
        return binarySearch(arr, data, start, pivot-1)

print(binarySearch(arr, 8, 0, len(arr)-1))
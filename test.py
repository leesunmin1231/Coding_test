def partition(arr, start, end):
    i = start
    pivot = arr[i]
    for j in range(start+1, end+1):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
    arr[start] = arr[i]
    arr[i] = pivot
    return i
def quickSort(arr, start, end):
    if start >= end:
        return
    q = partition(arr, start, end)
    quickSort(arr, start, q)
    quickSort(arr, q+1, end)

def solution(array, commands):
    answer = []
    for cmd in commands:
        splitArray = array[cmd[0]-1:cmd[1]]
        quickSort(splitArray,0,cmd[1]-cmd[0])
        answer.append(splitArray[cmd[2]-1])
    return answer
array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)
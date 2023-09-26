def combination(arr, count):
    if count == 1:
        return [[x] for x in arr]
    result = []
    for index, target in enumerate(arr):
        rest = combination(arr[index+1:], count-1)
        tmp = [[target]+ x for x in rest]
        result.extend(tmp)
    return result

print(combination([1,2,3,4], 2))
def solution(triangle):
    dist = []
    first = triangle.pop(0)
    dist.append([0] + first + [0])
    for row in triangle:
        tmp = [0] + row + [0]
        prev = dist[-1]
        for i in range(1, len(row)+1):
            tmp[i] += max([prev[i-1], prev[i]])
        dist.append(tmp)
    return max(dist[-1])
def solution(routes):
    routes.sort(key=lambda x:x[1])
    camera = -30001
    ans = 0
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            ans += 1
    return ans
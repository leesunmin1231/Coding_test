from itertools import combinations_with_replacement

def solution(n, info):
    info.reverse()
    scores = [0,1,2,3,4,5,6,7,8,9,10]
    result = combinations_with_replacement(scores, n)
    ans = [[-1]]
    maxScore = 1
    for res in result:
        lion = [0] * 11
        lionTotal = 0
        apeachTotal = 0
        tmp = list(res)
        for score in tmp:
            lion[score] += 1
        for score in scores:
            a = info[score]
            l = lion[score]
            if l == a == 0:
                continue
            if l > a:
                lionTotal += score
            else:
                apeachTotal += score
        lion.reverse()
        if lionTotal - apeachTotal > maxScore:
            ans.clear()
            ans.append(lion)
            maxScore = lionTotal - apeachTotal
        if lionTotal - apeachTotal == maxScore:
            ans.append(lion) 
    if ans[0][0] == -1:
        return [-1]
    ans.sort(reverse=True, key=lambda x:(x[10],x[9],x[8],x[7],x[6],x[5],x[4],x[3],x[2],x[1],x[0]))
    return ans[0]
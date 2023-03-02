def solution(lotteries):
    number = 0
    maxPercent = 0
    maxPrice = 0
    for i,lotter in enumerate(lotteries):
        buyer = lotter[1]+1
        percent = lotter[0]/buyer
        if percent > 1:
            percent = 1
        if percent > maxPercent:
            maxPercent = percent
            maxPrice = lotter[2]
            number = i+1
        elif percent == maxPercent:
            if maxPrice < lotter[2]:
                maxPrice = lotter[2]
                number = i+1
    return number


lotteries = [[100,100,500],[1000,1000,100]]
print(solution(lotteries))
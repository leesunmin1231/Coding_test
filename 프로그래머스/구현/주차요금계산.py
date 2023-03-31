import math

def getTotalTime(inTime, outTime):
    Intime = list(map(int, inTime.split(":")))
    Outtime = list(map(int, outTime.split(":")))
    return (Outtime[0]*60 + Outtime[1]) - (Intime[0]*60 + Intime[1])

def solution(fees, records):
    In = []
    totalTimes = {}
    for record in records:
        data = record.split(" ")
        if data[2] == "IN":
            In.append(data)
        else:
            inTime = ''
            tmp = []
            for i in In:
                if i[1] == data[1]:
                    inTime = i[0]
                else:
                    tmp.append(i)
            In = tmp
            term = getTotalTime(inTime, data[0])
            if data[1] in totalTimes:
                totalTimes[data[1]] += term
            else:
                totalTimes[data[1]] = term
    for data in In:
        term = getTotalTime(data[0], "23:59")
        if data[1] in totalTimes:
            totalTimes[data[1]] += term
        else:
            totalTimes[data[1]] = term
    ans = []
    for key,value in totalTimes.items():
        fee = fees[1] + math.ceil((value - fees[0])/fees[2]) * fees[3]
        if value <= fees[0]:
            fee = fees[1]
        ans.append([key, fee])
    return [x[1] for x in sorted(ans, key=lambda x:x[0])]
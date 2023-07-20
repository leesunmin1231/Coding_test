function convertToMin(time){
    const [hour, min] = time.split(":").map((x) => Number(x))
    return hour * 60 + min
}

function getParkFee(totalTime, fees){
    const [defaultTime, defaultFee, term, termFee] = fees;
    let tmp = totalTime - defaultTime;
    if (tmp <= 0) return defaultFee
    return defaultFee + Math.ceil(tmp / term) * termFee;
}

function solution(fees, records) {
    const parking = {}
    const totalParkingTime = {}
    for (const record of records){
        const [time, num, type] = record.split(" ")
        if (type === "IN"){
            parking[num] = time
        } else{
            const totalTime = convertToMin(time) - convertToMin(parking[num])
            delete parking[num]
            if (totalParkingTime[num]){
                totalParkingTime[num] += totalTime
            }else{
                totalParkingTime[num] = totalTime
            }
        }
    }
    for (const [key, value] of Object.entries(parking)){
        const totalTime = convertToMin('23:59') - convertToMin(value)
        if (totalParkingTime[key]){
            totalParkingTime[key] += totalTime
        }else{
            totalParkingTime[key] = totalTime
        }
    }
    return Object.entries(totalParkingTime)
        .sort((prev, next) => prev[0] - next[0])
        .map((item) => getParkFee(item[1], fees))
}
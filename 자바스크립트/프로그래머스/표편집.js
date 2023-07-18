function solution(n, k, cmd) {
    let answer = Array(n).fill('O')
    const dq = []
    for (const line of cmd){
        const [type, num] = line.split(" ")
        // console.log(k, answer)
        if (type === 'D'){
            let i = 0;
            while (true){
                if (answer[k] === "O" && i >= Number(num)) break
                if (k === n-1) break;
                if (answer[k] !== 'X') {
                    i++;
                }
                k++;
            }
        }
        if (type === "U"){
            let i = 0;
            while (true){
                if (answer[k] === "O" && i >= Number(num)) break
                if (k === 0) break;
                if (answer[k] !== 'X') {
                    i++;
                }
                k--;
            }
        }
        if (type === 'C'){
            dq.push(k)
            const start = k;
            let i = 0;
            while(true){
                if (answer[k] === "O" && i >= 1) break
                if (k === n) break;
                if (answer[k] !== 'X'){
                    i++;
                }
                k++;
            }
            if (k === n){
                i = 0;
                k = start;
                while(true){
                    if (answer[k] === "O" && i >= 1) break
                    if (k === 0) break;
                    if (answer[k] !== "X") {
                        i++;
                    }
                    k--;
                }
            }
            answer[start] = 'X'
        }
        if (type === "Z"){
            const tmp = dq.pop()
            answer[tmp] = 'O'
        }
    }
    return answer.join("")
}
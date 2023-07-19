
const fs = require('fs');
// const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputs = fs.readFileSync('./자바스크립트/백준/컴백홈/exemple.txt').toString().trim().split('\n');

const [R, C, K] = inputs[0].split(" ").map((x) => Number(x))
const board = []
for (let i = 1; i < inputs.length; i++){
    board.push([...inputs[i]])
}


function solution(board, R, C, K){
    const start = [R-1, 0]
    const end = [0, C - 1]
    const dist = Array.from(Array(R), () => Array(C).fill(0))
    const q = []
    q.push(start)
    let ans = 0;
    while (q.length !== 0){
        const [r, c] = q.shift()
        if (r === end[0] && c === end[1]){
            for (const row of dist){
                console.log(row)
            }
            console.log("\n")
            console.log(q)
            if (dist[r][c] === K) ans++;
            continue
        }
        for (const [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]){
            if (nr < 0 || nr >= R) continue
            if (nc < 0 || nc >= C) continue
            if (board[nr][nc] === "T") continue
            if (dist[nr][nc] !== 0) continue
            dist[nr][nc] = dist[r][c] + 1
            q.push([nr, nc])
        }
    }
    return ans
}

console.log(solution(board, R,C, K))
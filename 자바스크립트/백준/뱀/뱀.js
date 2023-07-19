const fs = require('fs');
// const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputs = fs.readFileSync('./자바스크립트/백준/뱀/exemple.txt').toString().trim().split('\n');
let [N, K, ...arr] = inputs

const apples = arr.slice(0,K)
const [L, ...directions] = arr.slice(Number(K), arr.length)

function changeDir(current, rotate){
    if (rotate === "L"){
        switch(current){
            case 0:
                return 3
            case 1:
                return 2
            case 2:
                return 0
            default:
                return 1
        }
    } else if (rotate === "D"){
        switch(current){
            case 0:
                return 2
            case 1:
                return 3
            case 2:
                return 1
            default:
                return 0
        }
    }
    return current
}

function solution(N, board, dirObj, dirBoard){
    let timer = 0
    let dir = 0
    // 오른쪽, 왼쪽, 아래, 위
    const dr = [0,0,1,-1]
    const dc = [1,-1,0,0]
    let [headR, headC] = [0,0]
    let [tailR, tailC] = [0,0]
    while (true){
        // 방향 바꾸기
        dir = changeDir(dir, dirObj[String(timer)])
        
        // 벽에 부딪히는경우
        if(headR + dr[dir] >= N || headR + dr[dir] < 0) return timer
        if(headC + dc[dir] >= N || headC + dc[dir] < 0) return timer
        // 몸에 부딪히는 경우
        if(board[headR+dr[dir]][headC+dc[dir]] === 2) return timer;
        // 머리이동
        dirBoard[headR][headC] = dir;
        headR += dr[dir]
        headC += dc[dir]
        // 사과가 없는 경우
        if (board[headR][headC] === 0){
            board[tailR][tailC] = 0
            const tailDir = dirBoard[tailR][tailC]
            tailR += dr[tailDir]
            tailC += dc[tailDir]
        }
        board[headR][headC] = 2
        timer++;
    }
}

N = Number(N)
const board = Array.from(Array(N), () => Array(N).fill(0))
const dirBoard = Array.from(Array(N), () => Array(N).fill(-1))
// 사과: 1, 뱀: 2, 빈공간:0
for (const apple of apples){
    const [r, c] = apple.split(" ")
    board[r-1][c-1] = 1
}
board[0][0] = 2
const dirObj = {}
for (const dir of directions){
    const [time, rotate] = dir.split(" ");
    dirObj[time] = rotate
}
console.log(solution(N, board, dirObj, dirBoard)+1)
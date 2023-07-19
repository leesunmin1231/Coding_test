
const fs = require('fs');
// const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputs = fs.readFileSync('./자바스크립트/백준/시험감독/exemple.txt').toString().trim().split('\n');
const N = inputs[0];
let A = inputs[1].split(" ").map((num)=> Number(num))
const [B, C] = inputs[2].split(" ").map((num)=> Number(num))
let count = 0;
for (const total of A) {
    if (total <= B) count++;
    else count += Math.ceil((total-B) / C) + 1
}
console.log(count);
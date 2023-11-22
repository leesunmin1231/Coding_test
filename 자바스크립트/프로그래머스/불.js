const readline = require("readline");

function solution(R, C, board) {
  let time = 0;
  let person = findPerson(board, R, C);
  let fires = findFires(board, R, C);
  const q = [];
  q.push([person, board]);
  while (q.length > 0) {
    time += 1;
    const [r, c] = q.shift();
    // 지훈이가 나갈 수 있는지 체크
    if (r === R - 1 || r === 0) return time;
    else if (c === C - 1 || c === 0) return time;
    // 지훈이 이동

    // 지훈이가 이동할 곳이 없는 경우 IMPOSSIBLE
    // 불 번짐
  }
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let R = null;
  let C = null;
  let count = 0;
  const data = [];

  for await (const line of rl) {
    if (!R) {
      [R, C] = line.split(" ").map((x) => Number(x));
    } else {
      data.push(line);
      count += 1;
    }
    if (R === count) {
      rl.close();
    }
  }
  solution(R, C, data);
  process.exit();
})();

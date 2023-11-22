// https://velog.io/@grap3fruit/%EA%B5%AC%EB%A6%84goorm-%EC%BD%94%ED%85%8C-javascript-%EB%A1%9C-%EC%9E%85%EB%A0%A5%EA%B0%92-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let count = 0;
  const data = [];

  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else {
      data.push(line);
      count += 1;
    }
    if (N === count) {
      rl.close();
    }
  }
  solution(N, data);
  process.exit();
})();

// 테케가 여러개 인 경우 (T가 있는 경우)

const solution = (N, data) => {
  console.log(N);
  console.log(data);
};

let T = null;
let N = null;
let info = null;
let countN = 0;
let countT = 0;
let data = [];

rl.on("line", function (line) {
  if (!T) {
    T = +line;
  } else if (!N) {
    N = +line;
  } else {
    data.push(line);
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line.split(' ').map((el) => +el));
    countN += 1; // data를 입력받으면 countN을 증가시켜주고
  }
  if (countN === N) {
    // N만큼 data를 잘 입력 받았으면
    solution(N, data); // solution을 호출하고
    N = null; // T, countT를 제외한 값들을 초기화해준다.
    info = null;
    countN = 0;
    data = [];

    countT += 1; // 그리고 테스트 케이스 하나를 통과했으니 countT를 1 올려준다.
  }
  if (countT === T) {
    // 입력받은 T 만큼 테스트 케이스를 통과하게되면
    rl.close(); // rl.close()를 호출하고
  }
}).on("close", function () {
  process.exit(); // 종료한다.
});

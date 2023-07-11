function solution(targets) {
  targets.sort((prev, next) => prev[1] - next[1]);
  let tmp = -1;
  let ans = 0;
  for (const target of targets) {
    const [start, end] = target;
    if (start > tmp) {
      ans += 1;
      tmp = end - 0.5;
    }
  }
  return ans;
}
// 그리디

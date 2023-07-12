function solution(numbers, target) {
  const stack = [];
  const endPoint = numbers.length;
  let ans = 0;
  stack.push([numbers[0], 1]);
  stack.push([-numbers[0], 1]);
  while (stack.length !== 0) {
    const [sum, nextIdx] = stack.pop();
    if (nextIdx === endPoint) {
      if (sum === target) ans++;
      continue;
    }
    stack.push([sum + numbers[nextIdx], nextIdx + 1]);
    stack.push([sum - numbers[nextIdx], nextIdx + 1]);
  }
  return ans;
}

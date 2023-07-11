function solution(r1, r2) {
  let count = 0;
  for (let x = 1; x < r2; x++) {
    let ystart = Math.ceil(Math.sqrt(r1 * r1 - x * x));
    if (isNaN(ystart)) {
      ystart = 0;
    }
    let yend = Math.floor(Math.sqrt(r2 * r2 - x * x));
    count += yend - ystart + 1;
  }
  return count * 4 + 4;
}

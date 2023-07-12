function parseTerms(terms) {
  const obj = {};
  for (const term of terms) {
    const [key, value] = term.split(" ");
    obj[key] = Number(value);
  }
  return obj;
}

function timeCalculate(start, term) {
  const [year, month, day] = start.split(".").map((x) => Number(x));
  let newMonth = month + term;
  let newYear = year;
  if (newMonth > 12) {
    newYear += Math.floor(newMonth / 12);
    newMonth = newMonth % 12;
  }
  if (newMonth === 0) {
    newYear -= 1;
    newMonth = 12;
  }
  return [newYear, newMonth, day].join(".");
}

function isExpire(today, limit) {
  const [year, month, day] = today.split(".").map((x) => Number(x));
  const [lyear, lmonth, lday] = limit.split(".").map((x) => Number(x));
  if (year > lyear) return true;
  if (year === lyear && month > lmonth) return true;
  if (year === lyear && month === lmonth && day >= lday) return true;
  return false;
}

function solution(today, terms, privacies) {
  const termsObj = parseTerms(terms);
  const ans = [];
  for (let i = 0; i < privacies.length; i++) {
    const [expireTime, key] = privacies[i].split(" ");
    if (isExpire(today, timeCalculate(expireTime, termsObj[key]))) {
      ans.push(i + 1);
    }
  }
  return ans;
}

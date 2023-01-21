// 문자열 게임 2

const fs = require('fs');
const [T, ...rest] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

function game(w, k) {
  if (k === 1) {
    answer.push('1 1');
    return;
  }

  const dict = {};
  const lengthList = [];
  const stringList = w.split('');

  stringList.forEach((string, idx) => {
    if (!dict[string]) {
      dict[string] = [idx];
    } else {
      dict[string].push(idx);
    }
  });

  for (let word of Object.keys(dict)) {
    const wordLength = dict[word].length;
    if (wordLength < k) continue;

    if (wordLength === k) {
      lengthList.push(dict[word][wordLength - 1] - dict[word][0] + 1);
    } else {
      for (let i = 0; i <= wordLength - k; i++) {
        lengthList.push(dict[word][i + k - 1] - dict[word][i] + 1);
      }
    }
  }

  if (!lengthList.length) {
    answer.push(-1);
  } else answer.push(`${Math.min(...lengthList)} ${Math.max(...lengthList)}`);
}

let W, K;
const answer = [];

for (let i = 0; i < 2 * T; i++) {
  if (i % 2 === 0) {
    W = rest[i];
  } else {
    K = Number(rest[i]);
    game(W, K);
  }
}

console.log(answer.join('\n').trim());

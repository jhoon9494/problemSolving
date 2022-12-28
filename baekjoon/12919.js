// A와 B 2

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const S = input[0];
const T = input[1];

function game(t) {
  if (S === t) {
    return (result = 1);
  }

  if (S.length >= t.length) {
    return;
  }

  if (t[t.length - 1] === 'A') {
    const tList = t.split('');
    tList.pop();
    const newT = tList.join('');
    game(newT);
  }

  if (t[0] === 'B') {
    const tList = t.split('');
    tList.shift();
    const newT = tList.reverse().join('');
    game(newT);
  }
}

let result = 0;
game(T);
console.log(result);

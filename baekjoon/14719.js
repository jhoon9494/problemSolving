// 빗물

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = 1;
const block = [];
let h, w;

rl.on('line', (line) => {
  if (count === 1) {
    [h, w] = line
      .trim()
      .split(' ')
      .map((el) => Number(el));
    for (let i = 0; i < h; i++) {
      block.push([]);
      for (let j = 0; j < w; j++) {
        block[i].push(0);
      }
    }
    count++;
  } else {
    const height = line
      .trim()
      .split(' ')
      .map((el) => Number(el));

    for (let i = 0; i < height.length; i++) {
      for (let j = 1; j <= height[i]; j++) {
        block[h - j][i] = 1;
      }
    }

    rl.close();
  }
}).on('close', () => {
  let sum = 0;
  for (let i = 0; i < h; i++) {
    let start = -1;

    for (let j = 0; j < w; j++) {
      if (start < 0 && block[i][j] === 1) {
        start = j;
        continue;
      }
      if (start >= 0 && block[i][j] === 1) {
        sum += j - start - 1;
        start = j;
        continue;
      }
    }
  }

  console.log(sum);
});

// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let input = 1;
let cnt = 0;

while (input > 0) {
  cnt++;
  if (cnt.toString().includes("666")) {
    input--;
  }
}

console.log(cnt);

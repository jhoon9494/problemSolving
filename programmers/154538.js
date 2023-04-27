// 숫자 변환하기
class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }

  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  }

  add(value) {
    if (!this.size()) {
      this.storage[0] = value;
    } else {
      this.rear += 1;
      this.storage[this.rear] = value;
    }
  }

  popleft() {
    if (!this.size()) return undefined;

    const popItem = this.storage[this.front];
    delete this.storage[this.front];
    if (this.front === this.rear) {
      this.front = 0;
      this.rear = 0;
    } else {
      this.front += 1;
    }
    return popItem;
  }
}

function BFS(x, y, calc) {
  if (x === y) return 0;

  const q = new Queue();
  q.add([y, 0]);
  let answer = -1;

  while (q.size()) {
    const [currY, count] = q.popleft();
    for (let i = 0; i < 3; i++) {
      // x는 자연수이므로 x -> y로 계산할 경우, 계산된 수는 모두 자연수이므로 모두 고려해야함.
      // y -> x로 계산할 경우, 3이나 2로 나누는 계산에서 실수가 나올 수 있으므로 경우의 수가 줄어듦.
      let ny;
      if (i === 2) {
        ny = currY - calc[i];
      } else {
        ny = currY / calc[i];
      }

      // 정수가 아니거나 ny가 x보다 작을 경우 더 이상 진행하더라도 x는 될 수 없음.
      if (!Number.isInteger(ny) || ny < x) continue;
      if (ny > x) {
        q.add([ny, count + 1]);
        continue;
      }

      // BFS로 풀이했으므로, 계산된 ny가 x와 같다면 그 때 count가 최소 연산 횟수임.
      if (ny === x) {
        answer = count + 1;
        return answer;
      }
    }
  }
  return answer;
}

function solution(x, y, n) {
  const calc = [3, 2, Number(n)];
  return BFS(Number(x), Number(y), calc);
}

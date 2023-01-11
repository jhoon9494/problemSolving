// 녹색 옷 입은 애가 젤다지?

class Heap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
  getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
  getParentIndex = (childIndex) => Math.floor((childIndex - 1) / 2);

  insert = (key, value) => {
    const node = { key, value };
    this.heap.push(node);
    this.heapifyUp(); // 배열에 가장 끝에 넣고, 다시 min heap 의 형태를 갖추도록 한다.
  };

  // 최근에 삽입된 노드가 제 자리를 찾아갈 수 있도록 하는 메소드
  heapifyUp = () => {
    let index = this.heap.length - 1;
    const lastInsertedNode = this.heap[index];

    // 루트노드가 되기 전까지
    while (index > 0) {
      const parentIndex = this.getParentIndex(index);

      if (this.heap[parentIndex].key > lastInsertedNode.key) {
        this.heap[index] = this.heap[parentIndex];
        index = parentIndex;
      } else break;
    }

    this.heap[index] = lastInsertedNode;
  };

  remove = () => {
    const count = this.heap.length;
    const rootNode = this.heap[0];

    if (count <= 0) return undefined;
    if (count === 1) this.heap = [];
    else {
      this.heap[0] = this.heap.pop(); // 끝에 있는 노드를 부모로 만들고
      this.heapifyDown(); // 다시 min heap 의 형태를 갖추도록 한다.
    }

    return rootNode;
  };

  // 변경된 루트노드가 제 자리를 찾아가도록 하는 메소드
  heapifyDown = () => {
    let index = 0;
    const count = this.heap.length;
    const rootNode = this.heap[index];

    // 계속해서 left child 가 있을 때 까지 검사한다.
    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);

      // 왼쪽, 오른쪽 중에 더 작은 노드를 찾는다
      const smallerChildIndex =
        // rightChild 가 있다면 key의 값을 비교해서 더 작은 값을 찾는다.
        // 없다면 leftChild 가 더 작은 값을 가지는 인덱스가 된다.
        rightChildIndex < count &&
        this.heap[rightChildIndex].key < this.heap[leftChildIndex].key
          ? rightChildIndex
          : leftChildIndex;

      // 자식 노드의 키 값이 루트노드보다 작다면 위로 끌어올린다.
      if (this.heap[smallerChildIndex].key <= rootNode.key) {
        this.heap[index] = this.heap[smallerChildIndex];
        index = smallerChildIndex;
      } else break;
    }

    this.heap[index] = rootNode;
  };
}

function result(n, graph, dist, caseCount) {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  const array = new Heap();

  if (graph.length > 0) {
    array.insert(graph[0][0], [0, 0]);
    dist[0][0] = graph[0][0];

    while (array.length !== 0) {
      const deleteItem = array.remove();
      if (!deleteItem) break;
      const [y, x] = deleteItem.value;
      const cost = deleteItem.key;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];

        if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
          if (dist[ny][nx] > graph[ny][nx] + cost) {
            dist[ny][nx] = graph[ny][nx] + cost;
            array.insert(graph[ny][nx] + cost, [ny, nx]);
          }
        } else {
          continue;
        }
      }
    }
    console.log('Problem ' + caseCount + ': ' + dist[n - 1][n - 1]);
  }
}

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const readline = require('readline');
let n;
let caseCount = 0;
let lineCount;
let graph = [];
let dist = [];
const INF = 1e9;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', (line) => {
  if (Number(line) || line === '0') {
    if (line === '0') {
      rl.close();
    }

    n = Number(line);
    graph = [];
    dist = [];
    lineCount = 0;
    caseCount++;
  } else {
    lineCount++;
    const rupeeList = line
      .trim()
      .split(' ')
      .map((el) => Number(el));

    graph.push(rupeeList);
    const tempList = [];
    for (let j = 0; j < n; j++) {
      tempList.push(INF);
    }
    dist.push(tempList);
    if (lineCount === n) {
      result(n, graph, dist, caseCount);
    }
  }
});

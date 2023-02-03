// 무인도 여행
function findMap(x, y, visited, maps, list) {
  if (visited[y][x] !== 0) return;
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  visited[y][x] = 1;
  list.push(Number(maps[y][x]));

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if ((nx >= 0) & (ny >= 0) && nx < visited[0].length && ny < visited.length) {
      if (visited[ny][nx] === -1) continue;
      findMap(nx, ny, visited, maps, list);
    }
  }
}

function solution(maps) {
  const visited = [];
  const mapLength = maps[0].length;

  for (let i = 0; i < maps.length; i++) {
    let temp = [];
    for (let j = 0; j < mapLength; j++) {
      if (maps[i][j] === 'X') temp.push(-1);
      else temp.push(0);
    }
    visited.push(temp);
  }

  const answer = [];
  let sumList = [];
  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < mapLength; j++) {
      if (visited[i][j] === 0) {
        sumList = [];
        findMap(j, i, visited, maps, sumList);
        answer.push(sumList.reduce((acc, n) => acc + n));
      }
    }
  }
  if (answer.length === 0) {
    console.log([-1]);
  } else {
    console.log(answer.sort((a, b) => a - b));
  }
}

// solution(['X591X', 'X1X5X', 'X231X', '1XXX1']);
// solution(['XXX', 'XXX', 'XXX']);

// solution(['X1X', '123', 'X3X']);

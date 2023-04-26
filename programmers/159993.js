//미로 탈출
function makeVisitedList(rowLength, colLength) {
  const arr = [];
  for (let i = 0; i < colLength; i++) {
    const row = [];
    for (let j = 0; j < rowLength; j++) {
      row.push(-1);
    }
    arr.push(row);
  }

  return arr;
}

function findGoal(x, y, maps, goal) {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const rowLength = maps[0].length;
  const colLength = maps.length;
  const visited = makeVisitedList(rowLength, colLength);
  visited[y][x] = 0;
  const list = [[x, y]];

  while (list.length) {
    const [x, y] = list.shift();
    if (maps[y][x] === goal) return visited[y][x];

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < rowLength && ny < colLength && nx >= 0 && ny >= 0) {
        if (visited[ny][nx] === -1 && maps[ny][nx] !== 'X') {
          list.push([nx, ny]);
          visited[ny][nx] = visited[y][x] + 1;
        }
      }
    }
  }
}

function solution(maps) {
  const startVector = [];
  const leverVector = [];
  const exitVector = [];

  for (const y in maps) {
    const row = maps[y];
    for (const x in row) {
      const numX = Number(x);
      const numY = Number(y);
      if (row[x] === 'S') {
        startVector.push(numX, numY);
        continue;
      }

      if (row[x] === 'L') {
        leverVector.push(numX, numY);
        continue;
      }

      if (row[x] === 'E') {
        exitVector.push(numX, numY);
        continue;
      }
    }
  }
  const lengthToLever = findGoal(startVector[0], startVector[1], maps, 'L');
  const lengthToExit = findGoal(leverVector[0], leverVector[1], maps, 'E');

  if (!lengthToLever) return -1;

  if (!lengthToExit) return -1;

  return lengthToExit + lengthToLever;
}

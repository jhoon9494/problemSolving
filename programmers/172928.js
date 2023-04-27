// 공원 산책
function switchDirection(str) {
  switch (str) {
    case 'N': {
      return [0, -1];
    }
    case 'S': {
      return [0, 1];
    }
    case 'W': {
      return [-1, 0];
    }
    case 'E': {
      return [1, 0];
    }
  }
}

function move(x, y, park, route) {
  const [op, dist] = route.split(' ');
  const n = Number(dist);
  const dirVector = switchDirection(op);
  const h = park.length;
  const w = park[0].length;

  // 공원을 벗어나는지 확인
  const maxX = x + dirVector[0] * n;
  const maxY = y + dirVector[1] * n;
  if (maxX >= w || maxX < 0 || maxY >= h || maxY < 0) {
    return [y, x];
  }

  // 장애물을 만나는지 확인
  for (let i = 1; i <= n; i++) {
    const nx = x + dirVector[0] * i;
    const ny = y + dirVector[1] * i;

    if (park[ny][nx] === 'X') {
      return [y, x];
    }

    if (i === n) {
      return [ny, nx];
    }
  }
}

function solution(park, routes) {
  let startX = 0;
  let startY = 0;

  for (const y in park) {
    for (const x in park[y]) {
      if (park[y][x] === 'S') {
        startX = Number(x);
        startY = Number(y);
        break;
      }
    }
  }

  for (const route of routes) {
    const [y, x] = move(startX, startY, park, route);
    startX = x;
    startY = y;
  }

  return [startY, startX];
}

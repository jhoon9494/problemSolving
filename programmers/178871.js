// 달리기 경주
function solution(players, callings) {
  const playerObj = {};
  const list = [0, ...players];
  for (const index in players) {
    playerObj[players[index]] = Number(index) + 1;
  }

  for (const player of callings) {
    // list 상에서 순서 변경
    [list[playerObj[player] - 1], list[playerObj[player]]] = [
      list[playerObj[player]],
      list[playerObj[player] - 1],
    ];

    // 호명된 선수의 등수 증가
    playerObj[player] -= 1;

    // 호명된 선수와 교체된 선수의 등수 하락
    playerObj[list[playerObj[player] + 1]] += 1;
  }
  return list.slice(1);
}

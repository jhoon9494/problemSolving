// 요격 시스템
function solution(targets) {
  const sortedTargets = [...targets].sort((a, b) => a[0] - b[0]);

  let missile;
  let result = 0;
  for (const target of sortedTargets) {
    if (!missile) {
      missile = target;
      result++;
      continue;
    }

    if (target[0] < missile[1]) {
      missile[1] = Math.min(missile[1], target[1]);
    }

    if (target[0] >= missile[1]) {
      missile = target;
      result++;
      continue;
    }
  }

  return result;
}

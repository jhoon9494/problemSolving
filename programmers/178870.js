// 연속된 부분 수열의 합
function solution(sequence, k) {
  let start = 0;
  let end = 0;
  let numSum = sequence[end];
  const answer = [0, 1000000];

  while (start <= end) {
    if (numSum === k) {
      if (answer[1] - answer[0] > end - start) {
        answer[0] = start;
        answer[1] = end;
      }

      end++;
      if (end >= sequence.length) break;

      numSum += sequence[end];
      continue;
    }

    if (numSum < k) {
      end++;
      if (end >= sequence.length) break;

      numSum += sequence[end];
      continue;
    }

    if (numSum > k) {
      numSum -= sequence[start];
      start++;
      continue;
    }
  }
  return [answer[0], answer[1]];
}

# 보물상자 비밀번호
# import sys SWEA는 sys로 제춣되지 않음
from collections import deque
import itertools
# input = sys.stdin.readline

t = int(input())
count = 0

for i in range(2 * t):
  if i % 2 == 0:
    answer = []
    n, k = list(map(int, input().split()))
    continue
  else:
    numList = deque(list(input().strip()))
    count+=1

  # 보물상자 회전
  for j in range(n // 4):
    # 현재 회전에서 생성가능한 수
    for l in range(4):
      answer.append("".join(list(itertools.islice(numList, l * (n // 4), (l + 1) * (n // 4)))))

    lastItem = numList.pop()
    numList.appendleft(lastItem)

  print(f'#{count}', int(sorted(set(answer), reverse=True)[k-1], 16))
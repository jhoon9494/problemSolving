# 냅색문제
from itertools import combinations

n, c = map(int, input().split())
things = list(map(int,input().split()))

# Meet in the Middle 알고리즘
# 조합의 모든 경우의 수를 따질 경우 2^30의 경우의 수를 가짐.
# 그러나 반으로 나눌 경우 2^15의 경우의 수를 가지게 되어 시간복잡도를 단축 시킬 수 있음.
a_weight = things[:n//2]
b_weight = things[n//2:]
a_sum = []
b_sum = []

# 조합을 이용하여 가방에 넣을 물건들의 합에 대해 경우의 수 구하기
for i in range(len(a_weight)+1):
  cb_a = combinations(a_weight, i)
  for cb in cb_a:
    a_sum.append((sum(cb)))

for i in range(len(b_weight)+1):
  cb_b = combinations(b_weight, i)
  for cb in cb_b:
    b_sum.append((sum(cb)))

# 이진 탐색의 대상을 정렬
b_sum.sort()

# 이진 탐색
count = 0
for i in a_sum:
  if c - i < 0:
    continue
  
  start = 0
  end = len(b_sum) - 1

  while start <= end:
    mid = (start + end)//2

    if c - i < b_sum[mid]:
      end = mid -1
    else:
      start = mid + 1

  count += end + 1

print(count)
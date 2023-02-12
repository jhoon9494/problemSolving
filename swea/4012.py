# 요리사
from itertools import combinations

def divideGroup():
  comb = list(combinations([i for i in range(1, n+1)], n // 2))
  aGroup = comb[0 : len(comb) // 2]
  bGroup = comb[len(comb) : len(comb) // 2 - 1 : -1]
  return [aGroup, bGroup]

def calcSynergy(aIndex, bIndex):
  aSum = 0
  bSum = 0
  for i in aIndex:
    for j in aIndex:
      if i == j:
        continue
      aSum += table[i-1][j-1]

  for i in bIndex:
    for j in bIndex:
      if i == j:
        continue
      bSum += table[i-1][j-1]
  
  return abs(aSum - bSum)

t = int(input())
for tCase in range(t):
  n = int(input())
  table = [list(map(int, input().split())) for _ in range(n)]
  answer = [];

  aGroup, bGroup = divideGroup()
  for i in range(len(aGroup)):
    answer.append(calcSynergy(aGroup[i], bGroup[i]))
  print(f'#{tCase + 1} {min(answer)}')


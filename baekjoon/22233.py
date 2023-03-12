# 가희와 키워드

# 주어진 입력이 20만개씩 되기 때문에 배열로 찾을 경우 시간초과 발생함
# 해시맵을 사용해서 키로 접근한 후 처리해줘야 시간 초과가 발생하지 않음.
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

memo = dict()
for _ in range(n):
  memo[input().strip()] = 1

for i in range(m):
  keywords = input().rstrip().split(',')
  for k in keywords:
    if k in memo.keys():
      if memo.get(k, 0):
        del memo[k]
        n -= 1
  
  print(n)
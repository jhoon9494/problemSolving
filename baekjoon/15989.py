# 1,2,3 더하기 4
import sys
sys.setrecursionlimit(10000)

def find(number):
  if dp[number] != 0:
    return dp[number]
  
  dp[number] = find(number - 3) + (number // 2) + 1
  return dp[number]

t = int(input())

for _ in range(t):
  n = int(input())
  dp = [0, 1, 2, 3] + [0 for _ in range(n - 3)]
  print(find(n))

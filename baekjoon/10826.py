# 피보나치 수 4
import sys
sys.setrecursionlimit(100000)
n = int(input())

dp = [0 for _ in range(n+2)]
dp[1] = 1

def fibonacci(num):
  if num == 0:
    return dp[0]
  elif num == 1:
    return dp[1]
  elif dp[num] != 0:
    return dp[num]
   
  dp[num] = fibonacci(num-1)+fibonacci(num-2)
  
  if num == n:
    return dp[num]

  return fibonacci(num+1)

if n == 0:
  print(dp[0])
elif n == 1:
  print(dp[1])
else:
  print(fibonacci(2))
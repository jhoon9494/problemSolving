# 숫자 만들기
import math

def DFS(op, idx, sum):
  global maxSum, minSum
  if idx == n:
    maxSum = max(maxSum, sum)
    minSum = min(minSum, sum)
    return 

  for i in range(len(op)):
    if op[i] == 0:
      continue
    originSum = sum
    op[i] -= 1
    if i == 0:
      sum += nums[idx]
    elif i == 1:
      sum -= nums[idx]
    elif i == 2:
      sum *= nums[idx]
    else:
      sum = math.trunc(sum / nums[idx])
    DFS(op, idx + 1, sum)
    sum = originSum
    op[i] += 1

t = int(input())

for tCase in range(t):
  n = int(input())
  operator = list(map(int, input().split()))
  nums = list(map(int, input().split())) 
  maxSum = -1e9
  minSum = 1e9
  DFS(operator, 1, nums[0])
  print(f'#{tCase + 1} {maxSum - minSum}')
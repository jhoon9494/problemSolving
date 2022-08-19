# AC
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def func_result(p, array):
  R_count = 0
  last_index = len(p)-1
  result_array = deque(array[:])
  for index, func in enumerate(p):
    # R인 경우
    if func == "R":
      if R_count == 0:
        R_count = 1
      else:
        R_count = 0
      
      if index == last_index:
        if R_count == 1:
          return list(reversed(result_array))
        return list(result_array)

    # D인 경우
    else:
      if not result_array:
        return 'error'
      
      if R_count == 1:
        result_array.pop()
      else:
        result_array.popleft()

      if index == last_index:
        if R_count == 1:
          return list(reversed(result_array))
        return list(result_array)

for test_case in range(t):
  p = input().strip()
  n = int(input())
  if n > 0:
    temp = input().strip().strip('['']').split(',')
    array = list(map(int,temp))
  else:
    input()
    array = []
  result = func_result(p, array)

  if result == 'error':
    print(result)
  else:
    print("[", end="")
    print(*result, sep=",", end="")
    print("]")
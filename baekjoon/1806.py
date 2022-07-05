# 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int,input().split()))
result = []

start = 0
end = 0
list_sum = sequence[0]

while True:
  if list_sum < s:
    end += 1
    if end == n:
      break
    list_sum += sequence[end]
  else:
    result.append(end-start+1)
    list_sum -= sequence[start]
    start += 1
    if start > end:
      break
  
if len(result) == 0:
  print(0)
else:
  print(min(result))

# 두 수의 합

import sys
input = sys.stdin.readline

n = int(input())
sequence=list(map(int,input().split()))
# 정렬을 시켜야 투포인터를 사용할 수 있음.
sequence.sort()
x = int(input())

start = 0
end = len(sequence) -1
result = 0

while True:
  if start > end:
    break


  if start == end:
    list_sum = sequence[start]
  else:
    list_sum = sequence[start] + sequence[end]

  if list_sum > x:
    end -= 1
  else:
    start += 1
    if list_sum == x:
      result += 1

print(result)
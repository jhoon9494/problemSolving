# 색종이 만들기

import sys
input = sys.stdin.readline

n = int(input())
paper = [0 for _ in range(n)]

for i in range(n):
  paper[i] = list(map(int,input().split()))

blue_count = 0
white_count = 0
def divide_paper(n, start, column):
  global blue_count, white_count
  std_value = paper[column][start]

  for i in range(column, column + n):
    for j in range(start, start + n):
      if std_value != paper[i][j]:
        divide_paper(n//2, start, column)
        divide_paper(n//2, start+(n//2), column)
        divide_paper(n//2, start, column+(n//2))
        divide_paper(n//2, start+(n//2), column+(n//2))
        return

  if std_value == 1:
    blue_count += 1
  else:
    white_count += 1

divide_paper(n,0,0)
print(white_count)
print(blue_count)
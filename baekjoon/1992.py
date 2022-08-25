# 쿼드트리

import sys
input = sys.stdin.readline

n = int(input())
tree = [0 for _ in range(n)]

for i in range(n):
  tree[i] = input().strip()

result = ""
def quad_tree(n, column, row):
  global result
  std_value = tree[column][row]
  for i in range(column, column+n):
    for j in range(row, row+n):
      if std_value != tree[i][j]:
        result += "("
        quad_tree(n//2, column, row)
        quad_tree(n//2, column, row+(n//2))
        quad_tree(n//2, column+(n//2), row)
        quad_tree(n//2, column+(n//2), row+(n//2))
        result += ")"
        return 
  result += std_value


quad_tree(n, 0, 0)
print(result)
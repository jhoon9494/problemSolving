# 사이클 게임
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(value):
  if parent[value] == value:
    return value

  parent[value] = find(parent[value])
  return parent[value]

for i in range(m):
  a, b = map(int, input().split())
  findA = find(a)
  findB = find(b)

  if findA > findB:
    parent[findA] = findB
  elif findA < findB:
    parent[findB] = findA
  else:
    print(i+1)
    break

  if i == m-1:
    print(0)
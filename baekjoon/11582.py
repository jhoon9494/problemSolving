# 치킨 TOP N 
import sys
input = sys.stdin.readline

n = int(input())
score_list = list(map(int,input().split()))
k = int(input())



def sort_list(n, i):
  global sort_list, k
  while n//i >= 1:
    temp = []
    for j in range(n//i):
      new_list = score_list[j*i:(j*i)+i]
      temp.append(list(sorted(new_list)))
    sort_list = temp
    if n//i == k:
      break
    i *= 2
  return sort_list

print(str(sort_list(n,2)).replace("]","").replace("[","").replace(",",""))
# 치킨 TOP N 
import sys
input = sys.stdin.readline

n = int(input())
score_list = list(map(int,input().split()))
k = int(input())

# 문제 조건대로 n/2명 -> n/4명 -> n/8명 -> n/16명씩 순서대로 정렬하는 방식
# def sort_list(n, i):
#   global k
#   sorted_list=[]
  
#   while n//i >= 1:
#     temp = []
#     for j in range(n//i):
#       new_list = score_list[j*i:(j*i)+i]
#       temp.append(list(sorted(new_list)))
#     sorted_list = temp

#     k명의 회원이 정렬을 마친 뒤의 결과를 출력하기 위한 조건
#     if n//i == k:
#       break
#     i *= 2
#   return sorted_list

# print(str(sort_list(n,2)).replace("]","").replace("[","").replace(",",""))


for i in range(k):
  new_list = score_list[i * (n//k): (i * (n//k)) + n//k]
  for item in sorted(new_list):
    print(item, end=" ")
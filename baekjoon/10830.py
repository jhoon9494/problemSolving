# 행렬 제곱
import sys
input=sys.stdin.readline

n,b=list(map(int,input().split()))
graph=[]
for i in range(n):
  graph.append(list(map(lambda x:int(x)%1000,input().split())))


def multiple(list1,list2):
  result=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][k]+=list1[i][j]*list2[j][k]
  
  for i in range(n):
    for j in range(n):
      if result[i][j]>=1000:
        result[i][j]%=1000
  return result


def calcul(n):
  if n==1:
    return graph
  else: 
    temp_list=calcul(n//2)
    if n%2==0:
      return multiple(temp_list,temp_list)
    else:
      temp=multiple(temp_list,temp_list)
      return multiple(temp,graph)

for i in range(n):
  for j in range(n):
    print(calcul(b)[i][j], end=" ")
  print()
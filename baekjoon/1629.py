# 곱셈
A,B,C=map(int,input().split())

def calcul(a,b):
  if b==1:
    return a%C
  else:
    temp=calcul(a,b//2)
    if b%2==0:
      return temp*temp%C
    else:
      return temp*temp*a%C

print(calcul(A,B))

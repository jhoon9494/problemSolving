# A → B

a,b=list(map(int,input().split()))
cnt=0
result=[]

def calcul(a):
  global cnt
  if a==b:
    result.append(cnt+1)
    return print(cnt+1)
  elif a>b:
    return result.append(-1)

  for i in range(2):
    if i==0:
      cnt+=1
      calcul(a*2)
      cnt-=1
    else:
      cnt+=1
      calcul(int(str(a)+"1"))
      cnt-=1

calcul(a)
if max(result)<0:
  print(-1)
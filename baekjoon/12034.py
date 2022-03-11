import sys
ss = sys.stdin.readline
T=int(ss())
case=0

while T>0:
  N=int(ss())
  price=list(map(int,ss().split()))

  result=[]
  case+=1
  visite=[9]*len(price)

  for i in range(len(price)):
    for j in range(len(price)):
      if price[i]%4!=0:
        break
      elif visite[j]==9 and price[i]*3/4 == price[j]:
        visite[i]=1
        visite[j]=0
        break

  for i in range(len(visite)):
    if visite[i]==0:
      result.append(str(price[i]))
  print(f'Case #{case}: {" ".join(result)}') 
  T-=1

  # import copy
  # 얕은 복사 vs 깊은 복사
  # 얕은 복사는 대입(=), [:] 슬라이싱, 객체.copy, copy.copy 
  # 얕은 복사란 변수를 복사했지만 참조한 곳은 동일하기 때문에 같은 변수를 가리키고 있는 것.
  # 깊은 복사는 copy.deepcopy
  # sale_price=copy.deepcopy(totalprice[i]) 
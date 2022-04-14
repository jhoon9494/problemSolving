# 거짓말
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
temp=list(map(int,input().split()))

true_group=[]
# 진실을 알고 있는 사람이 있을 때 리스트 생성 
if len(temp)>1:
  for i in range(1,len(temp)):
    true_group.append(temp[i])

party=[[] for _ in range(m)]
# 파티 참가자
for i in range(m):
  temp=list(map(int,input().split()))
  for j in range(1,temp[0]+1):
    party[i].append(temp[j])

# 과장된 이야기를 할 수 있는 파티 개수
allowed_party=[-1 for _ in range(m)]

# 진실을 알고 있는 사람
if true_group:
  for i in true_group:
    true_person=i
    for j in range(m):
      if true_person in party[j]:
        for k in party[j]:
          if k not in true_group:
            true_group.append(k)

  for i in range(len(true_group)):
    true_person=true_group[i]
    for j in range(m):
      if true_person not in party[j] and allowed_party[j]!=False:
        allowed_party[j]=True
      else:
        allowed_party[j]=False
else:
  for j in range(m):
    allowed_party[j]=True

cnt=0
for i in allowed_party:
  if i==True:
    cnt+=1
print(cnt)
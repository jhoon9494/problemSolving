import sys
ss=sys.stdin.readline

n=int(ss())
nums=list(map(int,ss().split()))
calcul=list(map(int,ss().split()))
result=[]

def dfs(start, dep):
  if dep==n-1:
    result.append(start)
    return result
  for i in range(4):
    if i==0 and calcul[i]>0:
      calcul[i]-=1
      dfs(start+nums[dep+1],dep+1)
      calcul[i]+=1
    if i==1 and calcul[i]>0:
      calcul[i]-=1
      dfs(start-nums[dep+1],dep+1)
      calcul[i]+=1
    if i==2 and calcul[i]>0:
      calcul[i]-=1 
      dfs(start*nums[dep+1],dep+1)
      calcul[i]+=1
    if i==3 and calcul[i]>0:
      calcul[i]-=1
      if start<0:
        start=abs(start)//nums[dep+1]
        dfs(-start,dep+1)
      else:
        dfs(start//nums[dep+1],dep+1)
      calcul[i]+=1

dfs(nums[0],0)
print(max(result))
print(min(result))
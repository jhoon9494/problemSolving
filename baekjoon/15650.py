# N과 M(2)

n,m=map(int,(input().split()))

def dfs(start,count):
  temp.append(str(start))
  if count==m:
    print(" ".join(temp))
    return
  for i in range(1,n+1):
    if i > start:
      dfs(i,count+1)
      temp.pop()
  
for i in range(1,n+1):
  temp=[]
  cnt=1
  dfs(i,cnt)
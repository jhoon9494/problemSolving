# 숨바꼭질 3
from collections import deque

n,m=map(int,input().split())
INF=1e9
dx=[-1,1,2]

def find(start,time):
  visited=[INF]*(m+1+abs(n-m))
  if start==m:
    visited[start]=time
  q=deque()
  q.append((start,time))

  while q:
    x,t=q.popleft()
    for i in range(3):
      if i==2:
        nx=x*dx[i]
      else: 
        nx=x+dx[i]
      
      if nx>=0 and m+abs(n-m)>nx and visited[nx]>t:
        if i!=2:
          visited[nx]=t+1
          q.append((nx,t+1))
        else:
          visited[nx]=t
          q.append((nx,t))
  return visited[m]

time=0
print(find(n,time))


# 유기농 배추
import sys
ss=sys.stdin.readline
from collections import deque

#좌, 우, 상, 하
dx=[-1,1,0,0] 
dy=[0,0,-1,1]

T=int(ss())
while(T>0):
  M,N,K=map(int,ss().split(" "))
  result=0
  ground=[[0]*M for _ in range(N)]
  visited=[[0]*M for _ in range(N)]

  for i in range(K):
    x,y=map(int,ss().split(" "))
    ground[y][x]=1

  def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
      x,y=q.popleft()
      for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]

        if 0<=nx<M and 0<=ny<N and ground[ny][nx]==1 and visited[ny][nx]==0:
          visited[ny][nx]=1
          q.append((nx,ny))

  for i in range(N):
    for j in range(M):
      if ground[i][j]==1 and visited[i][j]==0:
        visited[i][j]=1
        bfs(j,i)
        result+=1

  print(result)      
  T-=1
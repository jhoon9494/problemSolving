# 토마토
import sys
from collections import deque
ss=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

M,N=map(int,ss().split())
graph=[]
visited=[[0]*M for _ in range(N)]

for i in range(N):
  graph.append(list(map(int,ss().rstrip().split())))

def bfs():
  q=deque()
  for i in range(N):
    for j in range(M):
      if graph[i][j]==1 and visited[i][j]==0:
        q.append((j,i))

  while q:
    x,y=q.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if 0<=nx<M and 0<=ny<N and graph[ny][nx]==0 and visited[ny][nx]==0:
        visited[ny][nx]=visited[y][x]+1
        graph[ny][nx]=1
        q.append((nx,ny))
      
      if 0<=nx<M and 0<=ny<N and graph[ny][nx]==-1:
        continue
      
  for i in range(N):
    if 0 in graph[i]:      
      return -1
  return visited[y][x]

print(bfs())
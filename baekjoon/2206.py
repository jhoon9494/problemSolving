# 벽 부수고 이동하기
import sys
from collections import deque
ss=sys.stdin.readline

n,m=map(int,ss().split())
graph=[]
visited=[[[0]*m for _ in range(n)] for _ in range(2)]
for i in range(n):
  graph.append(list(map(int,ss().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(x,y,z):
  visited[z][y][x]=1
  q=deque()
  q.append((x,y,z))
  while q:
    x,y,z=q.popleft()
    if x==m-1 and y==n-1:
      return print(visited[z][n-1][m-1])
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if 0<=nx<m and 0<=ny<n and visited[z][ny][nx]==0 and graph[ny][nx]==0:
        visited[z][ny][nx]=visited[z][y][x]+1
        q.append((nx,ny,z))
      elif 0<=nx<m and 0<=ny<n and z==0 and graph[ny][nx]==1:
        visited[1][ny][nx]=visited[0][y][x]+1
        q.append((nx,ny,1))

  return print(-1)

BFS(0,0,0)
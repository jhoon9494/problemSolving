import sys
from collections import deque
ss=sys.stdin.readline

graph=[]
n,k=map(int,ss().split())
for i in range(n):
  graph.append(list(map(int,ss().split())))
visited=[[0]*n for _ in range(n)]
s,x,y=map(int,ss().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
  q=deque()
  temp=[]

  for i in range(n):
    for j in range(n):
      if graph[i][j]!=0:
        temp.append((graph[i][j],j,i))
        visited[i][j]=0
  # graph[i][j]의 값을 기준으로 temp 리스트 오름차순 정렬
  temp.sort(key=lambda x:x[0])

  for i in temp:
    q.append(i)

  while q:
    value,x,y=q.popleft()
      
    if visited[x][y]<s: 
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[ny][nx]==0 and visited[ny][nx]==0:
          graph[ny][nx]=value
          visited[ny][nx]=visited[y][x]+1
          q.append((value,nx,ny))      
    else:
      break

bfs()
print(graph[x-1][y-1])
# for i in range(n):
#   for j in range(n):
#     print(graph[i][j], end=" ")
#   print()

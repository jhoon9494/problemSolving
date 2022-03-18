# # 유기농 배추 
# bfs
# import sys
# ss=sys.stdin.readline
# from collections import deque

# #좌, 우, 상, 하
# dx=[-1,1,0,0] 
# dy=[0,0,-1,1]

# T=int(ss())
# while(T>0):
#   M,N,K=map(int,ss().split(" "))
#   result=0
#   ground=[[0]*M for _ in range(N)]
#   visited=[[0]*M for _ in range(N)]

#   for i in range(K):
#     x,y=map(int,ss().split(" "))
#     ground[y][x]=1

#   def bfs(x,y):
#     q=deque()
#     q.append((x,y))

#     while q:
#       x,y=q.popleft()
#       for i in range(4):
#         nx= x+dx[i]
#         ny= y+dy[i]

#         if 0<=nx<M and 0<=ny<N and ground[ny][nx]==1 and visited[ny][nx]==0:
#           visited[ny][nx]=1
#           q.append((nx,ny))

#   for i in range(N):
#     for j in range(M):
#       if ground[i][j]==1 and visited[i][j]==0:
#         visited[i][j]=1
#         bfs(j,i)
#         result+=1

#   print(result)      
#   T-=1

# dfs
import sys
sys.setrecursionlimit(10000) #파이썬의 기본 재귀 한도는 1000이고, 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해야 한다.
ss=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

T=int(ss())

while T>0:
  M,N,K=map(int,ss().split())
  ground=[[0]*M for _ in range(N)]
  visited=[[0]*M for _ in range(N)]
  result=0

  for i in range(K):
    x,y=map(int,ss().split())
    ground[y][x]=1

  def dfs(x,y):
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<M and 0<=ny<N and visited[ny][nx]==0 and ground[ny][nx]==1:
        visited[ny][nx]=1
        dfs(nx,ny)
    

  for i in range(N):
    for j in range(M):
      if ground[i][j]==1 and visited[i][j]==0:
        visited[i][j]=1
        dfs(j,i)
        result+=1
  print(result)
  T-=1
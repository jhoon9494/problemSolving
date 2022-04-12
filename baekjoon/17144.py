# 미세먼지 안녕
import sys
from collections import deque
input=sys.stdin.readline

r,c,t=map(int,input().split())
room=[]
for _ in range(r):
  room.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
air_cleaner=[]
result=[]
for i in range(r):
    if room[i][0]==-1:
      air_cleaner.append((0,i))
      

def cleaner():
  sum=0
  move_dust=[[-9]*c for _ in range(r)]
  x,y=air_cleaner[0]
  x,y2=air_cleaner[1]

  move_dust[y][x]=-1
  move_dust[y2][x]=-1
 
  # 공기청정기에서 왼쪽으로 공기정화
  for i in range(1,c):
    if i==1:
      move_dust[y][i]=0
      move_dust[y2][i]=0
    else:
      move_dust[y][i]=room[y][i-1]
      move_dust[y2][i]=room[y2][i-1]
  # 위쪽 공기청정 
  for i in range(y-1,-1,-1):
    move_dust[i][c-1]=room[i+1][c-1]
  for i in range(c-2,-1,-1):
    move_dust[0][i]=room[0][i+1]
  for i in range(1,y):
    move_dust[i][0]=room[i-1][0]
  # 아래쪽 공기청정
  for i in range(y2+1,r):
    move_dust[i][c-1]=room[i-1][c-1]
  for i in range(c-2,-1,-1):
    move_dust[r-1][i]=room[r-1][i+1]
  for i in range(r-2,y2,-1):
    move_dust[i][0]=room[i+1][0]
  
  for i in range(r):
    for j in range(c):
      if move_dust[i][j]!=-9:
        room[i][j]=move_dust[i][j]
      if room[i][j]!=-1:
        sum+=room[i][j]
  result.append(sum)

def dust(t):
  time=0
  while time<t:
    # 확산되는 누적 먼지의 양을 계산하기 위한 그래프 생성.
    amount_dust=[[0]*c for _ in range(r)]
    q=deque()
    for i in range(r):
      for j in range(c):
        if room[i][j]>0:
          q.append((j,i,room[i][j]))
          
    while q:
      x,y,current_dust=q.popleft()
      cnt=0
      # 확산될 먼지의 양
      diffusione_dust=current_dust//5
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        # 공기청정기가 없는 방향으로 먼지 확산
        if 0<=nx<c and 0<=ny<r and room[ny][nx]!=-1:
          # 인접한 방향에 확산될 먼지의 양을 누적
          amount_dust[ny][nx]+=diffusione_dust
          # room 그래프에도 누적된 먼지의 양을 반영
          room[ny][nx]=amount_dust[ny][nx]
          cnt+=1
      # 확산되고 남은 미세먼지를 누적된 먼지의 양에 합산하여 반영
      amount_dust[y][x]+=current_dust-diffusione_dust*cnt
      room[y][x]=amount_dust[y][x]
    cleaner()
    time+=1


dust(t)
print(result[t-1])
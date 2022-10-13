# 움직이는 미로 탈출
import sys
input = sys.stdin.readline
from collections import deque;

chess = [0 for _ in range(8)]
wall = []

for i in range(8):
  chess[i] = input()
  for j in range(len(chess[i])):
    if chess[i][j] == "#":
      wall.append((j,i))

dx = [1, -1, 0, 0, 1, 1, -1, -1, 0]
dy = [0, 0, 1, -1, 1, -1, 1, -1, 0]

def bfs(x, y, t):
  q = deque()
  q.append((x, y, t))

  while q:
    x, y, t = q.popleft()
    t_wall = []
    t_next_wall = []

    # 벽 좌표
    for i in range(len(wall)-1, -1, -1):
      t_wall.append((wall[i][0], wall[i][1] + t))
      t_next_wall.append((wall[i][0], wall[i][1] + t + 1))

      if t_wall[0][1] > 7:
        t_wall.pop(0)
        t_next_wall.pop(0)

    if len(t_wall) == 0:
      return 1

    # 캐릭터 이동
    for i in range(len(dx)):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        if (nx, ny) in t_wall:
          continue
        elif (nx, ny) in t_next_wall:
          continue
        else:
          q.append((nx, ny , t + 1))
  return 0  

print(bfs(0, 7, 0))
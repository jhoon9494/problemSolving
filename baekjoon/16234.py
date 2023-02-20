# 인구 이동
from collections import deque
import math

def checkLine(x, y, line):
  global isOpen
  q = deque()
  q.append((x, y))
  totalPopulation = 0
  count = 0

  while(q):
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and ny >= 0 and nx < n and ny < n and visited[ny][nx] == 0:
        population = abs(country[y][x] - country[ny][nx])
        if population >= l and population <= r:
          isOpen = True
          q.append((nx, ny))
          line.append((nx, ny))
          visited[ny][nx] = 1
          totalPopulation += country[ny][nx]
          count += 1
  
  if totalPopulation != 0:
    return math.floor(totalPopulation / count)


n, l, r = list(map(int,input().split()))
country = [list(map(int, input().split())) for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
time = 0

while(True):
  visited = [[0 for _ in range(n)] for _ in range(n)]
  isOpen = False
  
  # 국경선 체크 및 인구 이동
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        line = []
        result = checkLine(j, i, line)
        if line:
          for v in line:
            country[v[1]][v[0]] = result
  
  if not isOpen:
    print(time)
    break
  else:
    time += 1
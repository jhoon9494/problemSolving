# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):
  visited[y][x] = 0
  q = deque()
  q.append((x, y, visited[y][x]))

  while q:
    x, y, dist = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < m and ny < n and nx >= 0 and ny >= 0:
        if visited[ny][nx] < 0:
          if graph[ny][nx] == 0:
            visited[ny][nx] = 0
          else :
            visited[ny][nx] = dist + 1
            q.append((nx, ny, visited[ny][nx]))


dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      BFS(j, i)
      break

for i in range(n):
  for j in range(m):
    # 원래 갈 수 없는 땅인 위치는 0을 출력
    if graph[i][j] == 0:
      visited[i][j] = 0
    print(visited[i][j], end = " ")
  print()
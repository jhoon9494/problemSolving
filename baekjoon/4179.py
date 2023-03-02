# 불!
from collections import deque

def moveFire(vectors, maze):
  dx = (0, 0, -1, 1)
  dy = (-1, 1, 0, 0)
  
  for _ in range(len(vectors)):
    x, y = vectors.popleft()
    visited[y][x] = -1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx >= 0 and ny >= 0 and nx < c and ny <r:
        if maze[ny][nx] == "." and visited[ny][nx] == 0:
          fVectors.append((nx, ny))
          visited[ny][nx] = -1


def moveJ(x, y, maze, visited, fVectors):
  dx = (0, 0, -1, 1)
  dy = (-1, 1, 0, 0)
  visited[y][x] = 1
  q = deque()
  q.append((x, y, visited[y][x]))
  
  while q:
    # 불이 지훈이에게 닿지 않아야 하므로 불을 먼저 한 칸 움직인 다음에 지훈이가 움직일 방향을 정해준다.
    if fVectors:
      moveFire(fVectors, maze)
    for _ in range(len(q)):
      x, y, dist = q.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < c and ny <r:
          if maze[ny][nx] == "." and visited[ny][nx] == 0:
            visited[ny][nx] = dist + 1

            if nx == 0 or ny == 0 or nx == c - 1 or ny == r - 1:
              return visited[ny][nx]
            else:
              q.append((nx, ny, visited[ny][nx]))
  return "IMPOSSIBLE"


r, c = map(int, input().split())
maze = []
jVector = ()
fVectors = deque()
visited = [[0] * c for _ in range(r)]
# 지도를 입력 받을 때 지훈의 위치와 불의 위치를 확인해준다
for i in range(r):
  mazeRow = [*input()]
  for j, item in enumerate(mazeRow):
    if item == "J":
      jVector = (j, i)
    elif item == "F":
      fVectors.append((j, i))
  maze.append(mazeRow)

# 지훈이의 위치가 가장자리인 경우 즉시 탈출 가능하므로 1을 출력
if jVector[0] == c - 1 or jVector[1] == r - 1 or jVector[0] == 0 or jVector[1] == 0:
  print(1)
else:
  print(moveJ(jVector[0], jVector[1], maze, visited, fVectors))

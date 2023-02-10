# 등산로 조성

def dfs(x, y, dist, depth):
  global maxDist, k
  visited[y][x] = dist

  if maxDist < dist:
    maxDist = dist

  # 상, 하, 좌, 우
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < n and visited[ny][nx] == 0:
      dist += 1
      if depth == 0:
        if graph[y][x] > graph[ny][nx]:
          dfs(nx, ny, dist, depth)
          # dfs로 방문 후 방문 표시를 해제해야만 다른 봉우리에서 탐색을 할 수 있음.
          visited[ny][nx] -= dist
        # 최대 k만큼 깎을 수 있으므로, 무조건 k만큼 다 깎을 필요 없음.
        # 현재 위치의 높이보다 1만큼 적을 정도로만 깎는 것이 최선임.
        # k = 3이고 9 -> 10 -> 7인 경우 두번째 9에서 3만큼 다 깎는 다면 9 -> 6 -> 7로 2칸 밖에 이동할 수 없지만.
        # 0보다 1적은 8이 되도록 깎는다면 9->8->7로 3칸 즉 1칸 더 많이 이동할 수 있음.
        elif graph[ny][nx] - graph[y][x] + 1 <= k:
          subtractNumber = graph[ny][nx] - graph[y][x] + 1
          graph[ny][nx] -= subtractNumber
          depth += 1
          dfs(nx, ny, dist, depth)
          visited[ny][nx] -= dist
          graph[ny][nx] += subtractNumber
          depth -= 1
      else:
        if graph[y][x]> graph[ny][nx]:
          dfs(nx, ny, dist, depth)
          visited[ny][nx] -= dist
      dist -= 1
      



t = int(input())
count = 0

for i in range(2 * t):
  if i % 2 == 0:
    n, k = list(map(int,input().split()))
    count += 1
    continue
  else:
    maxHeight = 1
    maxDist = 1
    graph = [0 for _ in range(n)]
    for i in range(n):
      graph[i] = list(map(int, input().split()))
      maxValue = max(graph[i])
      if maxValue > maxHeight:
        maxHeight = maxValue
    
    for colIdx, col in enumerate(graph):
      for rowIdx, row in enumerate(col):
        if row == maxHeight:
          # colIdx = y축
          # rowIdx = x축
          visited = [[0 for _ in range(n)] for _ in range(n)]
          dfs(rowIdx, colIdx, 1, 0)
    print(f'#{count} {maxDist}')
      
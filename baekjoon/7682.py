# 틱택토
from collections import deque

def strCounter(str, board):
  cnt = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == str:
        cnt += 1
  return cnt


def compareCount(player, board):
  xCount = strCounter("X", board)
  oCount = strCounter("O", board)

  if player == "X":
    if xCount > oCount:
      return "X"
    else:
      return "invalid"
  else:
    if xCount == oCount:
      return "O"
    else:
      return "invalid"


def BFS(x, y, visited, board):
  # 상 하 좌 우 좌상 우상 좌하 우하
  dx = (0, 0, -1, 1, -1, 1, -1, 1)
  dy = (-1, 1, 0, 0, -1, -1, 1, 1)
  
  visited[y][x] = 1
  curr = board[y][x]
  q = deque()

  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    q.append((nx, ny, i, visited[y][x]))

  while q:
    x, y, dir, dist = q.popleft()

    if x >= 0 and y >= 0 and x < 3 and y < 3:
      if visited[y][x] == 0 and board[y][x] == curr:
        visited[y][x] = dist + 1
        q.append((x + dx[dir], y + dy[dir], dir, visited[y][x]))
        if visited[y][x] == 3:
          return compareCount(curr, board)  
  return False


def isFullBoard(board):
  for row in board:
    if "." in row:
      return False
  return True


def check(board):
  isFinished = False
  winner = ""

  # 가로, 세로, 대각선 방향으로 3칸을 이은 말이 있는지 확인
  for i in range(3):
    for j in range(3):
      if board[i][j] == ".":
        continue
      if not winner:
        visited = [[0 for _ in range(3)] for _ in range(3)]
        result = BFS(j, i, visited, board)
        if not result:
          continue
        elif result == "invalid":
          return "invalid"
        else: 
          isFinished = True
          winner = result
      elif board[i][j] == winner:
        continue
      else:
        visited = [[0 for _ in range(3)] for _ in range(3)]
        newResult = BFS(j, i, visited, board)
        if not newResult:
          continue
        else:
          if newResult != winner:
            return "invalid"
          
  # 3칸을 이은 말이 없더라도 게임 판이 가득찼다면 게임이 종료되므로 확인.
  # 가득차지 않았다면 아직 게임의 최종 상태가 아니므로 invalid를 반환
  if not isFinished:
    if not isFullBoard(board):
      return "invalid"
  
  return "valid"

while True:
  game = input()
  if game == 'end':
    break
  board = []
  for i in range(3):
    board.append([*game][i * 3 : i * 3 + 3])
  xCount = strCounter("X", board)
  oCount = strCounter("O", board)
  if xCount < oCount:
    print('invalid')
  elif xCount - oCount > 1:
    print('invalid')
  else:
    print(check(board))

# 벽돌 깨기
t = int(input())

# 벽돌의 숫자 - 1만큼 상하좌우로 벽돌 깨기
def breakBrick(x, y, number, bricks):
  global breakRange

  # 먼저 자기 자신을 깬 다음
  bricks[y][x] = 0 
  if breakRange < number:
    breakRange = number

  # 재귀를 이용하여 게임 배열 범위 내에서 상하좌우로 벽돌의 숫자 - 1만큼 벽돌 깨기
  for i in range(1, number):
    # 상
    if y - i  >= 0:
      # 해당 벽돌의 숫자가 1보다 큰 경우 상하좌우로 더 깨야 하기 때문에 재귀로 처리
      if bricks[y - i][x] > 1:
        breakBrick(x, y - i, bricks[y - i][x], bricks)
      else:
        bricks[y - i][x] = 0
    # 하
    if y + i < h:
      if bricks[y + i][x] > 1:
        breakBrick(x, y + i, bricks[y + i][x], bricks)
      else:
        bricks[y + i][x] = 0
    # 좌
    if x - i >= 0:
      if bricks[y][x - i] > 1:
        breakBrick(x - i, y, bricks[y][x - i], bricks)
      else:
        bricks[y][x - i] = 0
    # 우
    if x + i < w:
      if bricks[y][x + i] > 1:
        breakBrick(x + i, y, bricks[y][x + i], bricks)
      else:
        bricks[y][x + i] = 0


# 주어진 x축 에서 세로로 벽돌을 내리는 함수
def downBricks(bricks, x):
  tmpList = []
  for i in range(h):
    if bricks[i][x] > 0:
      tmpList.append(bricks[i][x])
      bricks[i][x] = 0
  
  for j in range(len(tmpList)):
    bricks[h - 1 - j][x] = tmpList.pop()


def countBricks(bricks):
  count = 0
  for i in range(h):
    for j in range(w):
      if bricks[i][j] > 0:
        count += 1
  return count


def game(cnt, bricks, x):
  global answer, breakRange
  copyBricks = [f[:] for f in bricks]
  
  for y in range(h):
    if copyBricks[y][x] != 0:
      breakBrick(x, y, copyBricks[y][x], copyBricks)

      minRange = x - breakRange + 1
      maxRange = x + breakRange
      if minRange < 0: 
        minRange = 0
      if maxRange >= w:
        maxRange = w

      for col in range(minRange, maxRange):
        downBricks(copyBricks, col)
      break

  if cnt == n:
    currCount = countBricks(copyBricks)
    if currCount < answer:
      answer = currCount
    return 

  for x in range(w):
    game(cnt + 1, copyBricks, x)



for tCase in range(t):
  n, w, h = list(map(int, input().strip().split()))
  originBricks = [list(map(int, input().strip().split())) for _ in range(h)]
  answer = 1e9

  for x in range(w):
    breakRange = 0
    game(1, originBricks, x)
  
  print(f'#{tCase + 1} {answer}')



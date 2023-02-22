# 특이한 자석
from collections import deque

def checkMagnetPole(gearIndex, dir):
  currGear = gear[gearIndex]
  gearDir[gearIndex] = dir
  for n in nextGear[gearIndex]:
    nextIndex = int(n)
    if gearDir[nextIndex] != 0:
      continue
    # 오른쪽 자석
    if nextIndex > gearIndex:
      if currGear[2] == gear[nextIndex][6]:
        continue
      else: 
        checkMagnetPole(nextIndex, -dir)
    # 왼쪽 자석
    else:
      if currGear[6] == gear[nextIndex][2]:
        continue
      else: 
        checkMagnetPole(nextIndex, -dir)

def rotate(gearNum, dir):
  if dir == 0:
    return 
  # 시계 방향으로 회전
  if dir == 1:
    gear[gearNum].appendleft(gear[gearNum].pop())
  # 반시계 방향으로 회전
  else:
    gear[gearNum].append(gear[gearNum].popleft())

t = int(input())

for tCase in range(t):
  k = int(input())
  gear = [deque(list(map(int, input().split()))) for _ in range(4)]
  nextGear = (("1"), ("0", "2"), ("1", "3"), ("2"))
  score = 0

  for _ in range(k):
    gearNumber, dir = map(int, input().split())
    gearDir = [0, 0, 0, 0]
    checkMagnetPole(gearNumber - 1, dir)

    for i in range(4):
      rotate(i, gearDir[i])

  for g in range(4):
    if gear[g][0] == 0:
      continue
    else:
      score += 2 ** g
  
  print(f'#{tCase + 1} {score}')
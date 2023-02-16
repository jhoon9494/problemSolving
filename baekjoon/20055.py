# 컨베이어 벨트 위의 로봇
from collections import deque

# 벨트를 회전시킨다.
def rotateBelt(belt):
  belt.appendleft(belt.pop())
  # 벨트가 회전하여 내리는 위치에 로봇이 위치해있다면, 로봇은 움직이지않고 삭제
  robotLocation.appendleft(0)
  robotLocation.pop()

# 로봇이 있다면 로봇을 움직인다.
def moveRobot():
  global durability

  for i in range(n-1, -1, -1):
    if robotLocation[i] == 0:
      continue

    # 움직인 후 로봇이 N번 째에 있다면 로봇을 폐기
    if i == n - 1:
      robotLocation[i] = 0
      continue

    if robotLocation[i] == 1 and robotLocation[i + 1] == 0 and conveyorBelt[i + 1] >= 1:
      robotLocation[i] = 0
      robotLocation[i + 1] = 1
      conveyorBelt[i + 1] -= 1
      if conveyorBelt[i + 1] == 0:
        durability += 1

# 로봇 승차
def getRobot():
  global durability

  # 승차 위치의 내구도가 1이상일 때만 올릴 수 있음
  # 로봇을 첫번째 승차 위치에 올리고 내구도 1 감소 
  if conveyorBelt[0] >= 1:
    robotLocation[0] = 1
    conveyorBelt[0] -= 1

    if conveyorBelt[0] == 0:
      durability += 1


n, k = map(int, input().split())
conveyorBelt = deque(list(map(int, input().split())))
robotLocation = deque([0] * n)
durability = 0
step = 0

while(True):
  step += 1
  rotateBelt(conveyorBelt)
  moveRobot()
  getRobot()
  
  if durability >= k:
    print(step)
    break
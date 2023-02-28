# 랭킹전 대기열 

def checkRoom(room, idx):
  if len(room) == m:
    wait[idx] = 1

def createRoom(level, name, rooms):
  room = [(level, name)]
  rooms.append(room)
  wait.append(0)
  checkRoom(room, len(rooms) - 1) 


def joinRoom(level, name):
  if not rooms:
    createRoom(level, name, rooms)
    return
  
  else:
    isJoin = False
    for idx, room in enumerate(rooms):
      if wait[idx] == 0 and abs(room[0][0] - level) <= 10:
        room.append((level, name))
        checkRoom(room, idx)
        isJoin = True
        break
      else:
        continue
    if not isJoin:
      createRoom(level, name, rooms)


p, m = map(int, input().split())
player = [0 for _ in range(p)]

for i in range(p):
  # level, nickname
  l, n = input().split()
  player[i] = (int(l), n)

rooms = []
wait = []
for p in player:
  joinRoom(p[0], p[1])

for idx, room in enumerate(rooms):
  if wait[idx] == 0:
    print("Waiting!")
  else:
    print("Started!")

  room.sort(key = lambda x: x[1])
  for p in room:
    print(p[0], p[1])
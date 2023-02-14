# 전구와 스위치

def switch(list, index):
  list[index] = 1 - list[index]
  if index == 0:
    list[index + 1] = 1 - list[index + 1]
  elif index == len(list)-1:
    list[index - 1] = 1- list[index - 1]
  else:
    list[index - 1] = 1- list[index - 1]
    list[index + 1] = 1- list[index + 1]


def changeState(curr, create, count):
  for i in range(1, len(curr)):
    # 직전 전구의 상태가 변화할 상태와 같은 경우 현재 전구 상태를 변화시키면 안됨.
    if curr[i - 1] == create[i -1]:
      continue
    else:
      switch(curr, i)
      count += 1
  
  if "".join(map(str,curr)) == "".join(map(str,create)):
    return count
  else:
    return -1



n = int(input())
curr = list(map(int,input()))
create = list(map(int,input()))

firstBulbChange = curr[:]
switch(firstBulbChange, 0)

answer = []
# 0번째 전구의 스위치를 누른 경우
first = changeState(curr, create, 0)
if first >= 0:
  answer.append(first)
# 0번째 전구의 스위치를 누르지 않은 경우
second = changeState(firstBulbChange, create, 1)
if second >= 0:
  answer.append(second)

if answer:
  print(min(answer))
else:
  print(-1)
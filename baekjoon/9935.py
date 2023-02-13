# 문자열 폭발

import sys
from collections import deque
input = sys.stdin.readline

originStr = deque(list(input().strip()))
bombStr = list(input().strip())
stack = []

while(originStr):
  stack.append(originStr.popleft())

  if len(stack) >= len(bombStr):
    tmpList = stack[len(stack)-len(bombStr): len(stack)]
    isSame = True
    for i in range(len(bombStr)):
      if tmpList[i] == bombStr[i]:
        continue
      else:
        isSame = False
        break
    
    if isSame:
      for _ in range(len(bombStr)):
        stack.pop()

answer = "".join(stack);
if answer == "":
  print("FRULA")
else:
  print(answer)
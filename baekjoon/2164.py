# 카드2
from collections import deque

n = int(input())
list = [i for i in range(1,n+1)]

queue = deque(list)

i = 0
while(len(queue) > 1):
  if i % 2 == 0:
    queue.popleft()
  else:
    temp = queue.popleft()
    queue.append(temp)
  
  i+=1

print(queue[0])
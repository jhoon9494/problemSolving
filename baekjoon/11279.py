# 최대 힙
import sys
input = sys.stdin.readline

def insert_heap(list, x):
  list.append(x)

  if len(list) > 2:
    last_index = len(list) - 1
    parent_index = last_index // 2
    
    while parent_index != 0:
      # 삽입노드의 값과 부모노드의 값을 비교하여 삽입 노드가 큰 경우 값과 위치를 변경
      if list[last_index] > list[parent_index]:
        list[last_index], list[parent_index] = list[parent_index], list[last_index]
        last_index = parent_index
        parent_index = last_index // 2
      else:
        break


def delete_heap(list):
  print(list[1])

  if len(list) <= 2:
    list.pop()
    return 
  # 맨 마지막 노드가 부모노드가 됨
  list[1] = list.pop()
  
  parent = 1
  left = parent * 2
  right = parent * 2 + 1
  max_index = parent
  
  while left < len(list):
    if list[parent] < list[left]:
      max_index = left
    if right < len(list) and list[max_index] < list[right]:
      max_index = right
    if max_index != parent:
      list[parent], list[max_index] = list[max_index], list[parent]
      parent = max_index
      left = parent * 2
      right = parent * 2 + 1
    else:
      break

n = int(input())
list = [0]    

for i in range(n):
  x = int(input())

  if x != 0:
    insert_heap(list, x)
  else:
    if len(list) <= 1:
      print(0)
    else:
      delete_heap(list)



# 절댓값 힙
import sys
input = sys.stdin.readline

def insert_heap(array, x, abs_x):
  array.append((x, abs_x))

  if len(array) > 2: 
    last_index = len(array)-1
    parent_index = last_index // 2

    while parent_index != 0:
      if array[last_index][1] < array[parent_index][1]:
        array[last_index], array[parent_index] = array[parent_index], array[last_index]
      elif array[last_index][1] == array[parent_index][1] and array[last_index][0] < array[parent_index][0]:
        array[last_index], array[parent_index] = array[parent_index], array[last_index]
      else:
        break
      last_index = parent_index
      parent_index = last_index // 2

def delete_heap(array):
  print(array[1][0])

  if len(array) <= 2:
    array.pop()
    return

  array[1] = array.pop()

  parent_index = 1
  left_index = parent_index * 2
  right_index = parent_index * 2 + 1
  min_index = parent_index

  while left_index < len(array):
    if array[parent_index][1] > array[left_index][1]:
      min_index = left_index
    elif array[parent_index][1] == array[left_index][1] and array[parent_index][0] > array[left_index][0]:
      min_index = left_index

    if right_index < len(array):
      if array[min_index][1] > array[right_index][1]:
        min_index = right_index
      elif array[min_index][1] == array[right_index][1] and array[min_index][0] > array[right_index][0]:
        min_index = right_index

    if min_index != parent_index:
      array[min_index], array[parent_index] = array[parent_index], array[min_index]
      parent_index = min_index
      left_index = parent_index * 2
      right_index = parent_index * 2 + 1

    else:
      break


n = int(input())
# 0번째 인덱스는 편의상 사용 X
array = [0]

for i in range(n):
  x = int(input())
  
  if x != 0:
    abs_x = abs(x)
    insert_heap(array, x, abs_x)
  else:
    if len(array) <= 1:
      print(0)
    else:
      delete_heap(array)
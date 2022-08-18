# 프린터
from collections import deque

priorities = [2,1,4,1]
location = 3

def solution(priorities, location):
  q = deque((index, docs) for index, docs in enumerate(priorities))
  result = []

  # 중요도에 따라 재정렬
  while(q):
    document = q.popleft()
    # 대기열의 마지막 문서인 경우 result 리스트에 추가
    if not q:
      result.append(document)

    for index, docs in enumerate(q):
      if document[1] >= docs[1]:
        # 리스트(q)의 모든 docs값 보다 document값이 크거나 같은 경우 출력을 위해 result 리스트에 추가 
        if index == len(q) - 1:
          result.append(document)
        continue
      else:
        # document값이 docs값보다 작은 경우 리스트(q)의 맨 뒤로 이동
        q.append(document)
        break

  # 정렬된 리스트(result)에서 location값을 통해 출력순서 확인 가능
  for index, item in enumerate(result):
    if item[0] == location:
      return index + 1
  

print(solution(priorities, location))
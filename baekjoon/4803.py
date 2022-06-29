# 트리
import sys
input = sys.stdin.readline


def union(x, y, parent):
  parentX = find(x, parent)
  parentY = find(y, parent)

  if parentX > parentY:
    parent[parentX] = parentY
    return "NO_CYCLE"

  if parentX < parentY:
    parent[parentY] = parentX
    return "NO_CYCLE"

  # 부모 값이 같을 경우 사이클이 형성됨.
  if parentX == parentY:
    return "CYCLE"


def find(value, parent):
  if parent[value] == value:
    return value
  
  parent[value] = find(parent[value], parent)
  return parent[value]

case = 1
while True:
  n, m = map(int,input().split())
  if n == 0 and m == 0:
    break

  # parent의 0번 인덱스는 사용하지 않음
  parent = [i for i in range(n+1)]
  cycle = []

  for i in range(m):
    a, b = map(int,input().split())
    # 사이클일 경우 횟수로 치지 않음.
    # 카운팅을 위해 별도 리스트 추가
    if union(a, b, parent) == 'CYCLE':
      cycle.append(a)
  
  # 전체 트리의 부모 값 갱신
  for i in range(1, n+1):
    find(i, parent)

  # set()으로 중복을 제거하여 전체 트리가 몇개인지 확인
  tree_list = list(set(parent[1:]))

  # cycle에 담긴 요소들의 부모를 cycle_set에 담아서 tree_list의 값과 비교
  cycle_set = set()
  for item in cycle:
    cycle_set.add(parent[item])

  result_count = 0
  for tree in tree_list:
    if tree in cycle_set:
      continue
    result_count+=1

  if result_count > 1:
    print("Case "+ str(case) + ": A forest of " + str(result_count) + " trees.")
  elif result_count == 1:
    print("Case "+ str(case) + ": There is one tree.")
  else :
    print("Case "+ str(case) + ": No trees.")
  case+=1

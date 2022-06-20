# 친구 네트워크
import sys
input = sys.stdin.readline

# 부모 요소 찾기
def getGroup(value):
  if group[value] == value:
    return value
  group[value] = getGroup(group[value])
  return group[value]

# 부모 요소가 다를 경우 b의 부모 요소를 a의 부모 요소로 합치기
def union(a, b):
  groupA = getGroup(a)
  groupB = getGroup(b)

  if groupA != groupB:
    group[groupB] = groupA
    # 친구 네트워크가 연결되면 친구 수가 합쳐지므로 각 친구 그룹의 수를 더함
    number[groupA] += number[groupB]
  return number[groupA]

case = int(input())
for _ in range(case):
  f = int(input())
  # 문자열을 키 값으로 사용하기 위해서 딕셔너리 자료형 사용
  group = dict()
  # 친구 네트워크 상 친구 숫자
  number = dict()
  for _ in range(f):
    a, b = input().split()

    if group.get(a) == None:
      group[a] = a
      number[a] = 1

    if group.get(b) == None:
      group[b] = b
      number[b] = 1

    print(union(a, b))
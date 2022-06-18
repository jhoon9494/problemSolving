# 집합의 표현
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline;

n, m = map(int,input().split())
parent = [i for i in range(n + 1)]

# 부모 찾기
def getParent(num):
  # 부모일 경우 parent의 값과 자기 자신의 값이 같음
  if(parent[num]==num):
    return num 
  # 부모가 아닌 경우 재귀
  parent[num]=getParent(parent[num])
  return parent[num]


for _ in range(m):
  f, a, b = map(int, input().split())
  parentA = getParent(a)
  parentB = getParent(b)
  if(f == 0): 
    # a, b의 값 끼리 비교하는 것이 아니라 부모 요소의 값을 비교
    # 부모 요소의 값이 작은 쪽이 큰 쪽의 부모 요소가 됨.
    # f == 1일 때, getParent 함수가 호출되면서 최종적으로 부모 요소가 확정될 수 있음.
    if(parentA > parentB):
      parent[parentA] = parentB
    else:
      parent[parentB] = parentA
      
  else:
    if(parentA == parentB):
      print("YES")
    else:
      print("NO")
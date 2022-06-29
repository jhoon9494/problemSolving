# 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

pre_order=[]
while True:
  try:
    num = int(input())
    pre_order.append(num)
  except:
    break

def post_order(start, end):
  if start > end:
    return
  root = pre_order[start] 

  left_start = start+1
  # 트리의 노드가 하나일 경우 아래 반복문이 동작 하지 않기 때문에
  # 무한 루프를 방지하기 위해 mid의 기본값을 end+1로 지정
  mid = end+1
  for i in range(start+1, end+1):
    if root < pre_order[i]:
      mid = i
      break

  # 왼쪽 서브트리
  post_order(left_start, mid-1)
  # 오른쪽 서브트리
  post_order(mid, end)
  print(root)

n = len(pre_order) - 1
post_order(0, n)

# 트리의 순회
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 메모리 초과
# n = int(input())
# inorder = list(map(int,input().split()))
# postorder = list(map(int,input().split()))
# preorder = [i for i  in range(n)]
# visited = [0 for _ in range(n+1)]
# root = postorder[len(postorder) - 1] 
# main_root_index = inorder.index(root)


# result = []
# def find_preorder(root):
#   global main_root_index
#   root_index = inorder.index(root)
#   result.append(str(root))
#   visited[root] = 1
#   if root_index <= main_root_index :
#     left_root_index = root_index -1 
#   else :
#     left_root_index = root_index -2
#   right_root_index = postorder.index(root)-1
#   left_root = postorder[left_root_index]
#   right_root = postorder[right_root_index]

#   if visited[left_root] == 0:
#     find_preorder(left_root)
  
#   if visited[right_root] == 0:
#     find_preorder(right_root)


# find_preorder(root)
# print(" ".join(result))

def preorder(in_start, in_end, post_start, post_end):
  if in_start > in_end or post_start > post_end:
    return
  
  root = postorder[post_end]
  inorder_root_index = idx[root]
  print(root, end=" ")

  dist = inorder_root_index - in_start
  
  # 왼쪽 서브트리
  preorder(in_start, inorder_root_index - 1 , post_start, post_start + dist - 1)
  # 오른쪽 서브트리
  # postorder의 왼쪽 서브트리 끝 바로 다음이 오른쪽 서브트리의 시작점
  preorder(inorder_root_index + 1, in_end, post_start + dist, post_end - 1)


n = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
idx = [0] * (n+1)

# 인오더의 인덱스를 반환
# idx[5] == 5의 인덱스 값 출력
# 5의 인덱스 == 인오더에서 5까지의 거리와 동일
for i in range(n): 
  idx[inorder[i]] = i

preorder(0, n-1, 0, n-1)
# 트리 순회
import sys
input = sys.stdin.readline

n = int(input())
graph = [i for i in range(n)]
nodeList = dict()
for i in range(n):
  node, left, right = input().split()
  nodeList[node] = i
  graph[i] = [left, right]

preorderList = []
inorderList = []
postorderList = []

def preorder(start):
  preorderList.append(start)
  
  for child in graph[nodeList[start]]:
    if(child != "."):
      preorder(child)

def inorder(start):
  for i in range(len(graph[nodeList[start]])):
    if i == 0:
      if graph[nodeList[start]][i] != ".":
        inorder(graph[nodeList[start]][i])
      else :
        continue
    else :
      inorderList.append(start)
      if graph[nodeList[start]][i] != ".":
        inorder(graph[nodeList[start]][i])
      else:
        continue

def postorder(start):
  for i in range(len(graph[nodeList[start]])):
    if i == 0:
      if graph[nodeList[start]][i] != ".":
        postorder(graph[nodeList[start]][i])
      else :
        continue
    else :
      if graph[nodeList[start]][i] != ".":
        postorder(graph[nodeList[start]][i])
      else:
        continue
  postorderList.append(start)

preorder("A")
inorder("A")
postorder("A")

print("".join(preorderList))
print("".join(inorderList))
print("".join(postorderList))

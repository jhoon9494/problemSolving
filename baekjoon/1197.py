# 최소 스패닝 트리
def find(value):
  if parent[value] == value:
    return value
  
  parent[value] = find(parent[value])
  return parent[value]

def isCycle(a, b):
  parentA = find(a)
  parentB = find(b)

  if parentA < parentB:
    parent[parentB] = parentA
    return False
  elif parentA > parentB:
    parent[parentA] = parentB
    return False
  else:
    return True

v, e = list(map(int,input().split()))
graph = [0 for _ in range(e)]
parent = [i for i in range(v + 1)]
vCount = 0
answer = 0
for i in range(e):
  a,b,c = list(map(int,input().split()))
  graph[i] = (c, (a ,b))

graph.sort(key = lambda x:x[0], reverse = True)

while(True):
  item = graph.pop()
  weightValue = item[0]
  vectorA, vectorB = item[1]

  if isCycle(vectorA, vectorB):
    continue
  else:
    answer += weightValue
    vCount += 1

  if vCount == v - 1:
    break

print(answer)
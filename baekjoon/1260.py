# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline;

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[a].sort()
  graph[b].append(a)
  graph[b].sort()


def BFS(start):
  q=deque()
  visited[start] = 1
  result=[]
  result.append(start)

  for i in graph[start]:
    q.append(i)

  while(q):
    vertex = q.popleft()
    
    if visited[vertex] != 1:
      visited[vertex] = 1
      result.append(vertex)
      for i in graph[vertex]:
        q.append(i)

  print(' '.join(map(str,result)))


result=[]
def DFS(start):
  result.append(start)
  visited[start]=1
  if(len(graph[start])==0):
    return

  for i in graph[start]:
    if visited[i] == 0:
      DFS(i)

DFS(v)
print(' '.join(map(str,result)))

# bfs를 위해 visited 배열 초기화
visited = [0 for _ in range(n+1)]
BFS(v)
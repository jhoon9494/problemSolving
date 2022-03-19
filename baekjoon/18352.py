# 특정 거리의 도시 찾기
import sys
from collections import deque
ss=sys.stdin.readline

n,m,k,x=map(int,ss().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
  a,b=list(map(int,ss().split()))
  graph[a].append(b)

def bfs(num):
  q=deque()
  q.append(num)
  visited[num]=1
  result=[]

  while q:
    x=q.popleft()
    # for x in graph[x]: 
    #  if visited[x] == 0:     
    # 변수를 추가로 작성하는 것 보다 위의 코드로 작성하는 것이 좀더 간결함.
    nx=graph[x]
    for i in range(len(nx)):
      if visited[nx[i]]==0:
        q.append(nx[i])
        visited[nx[i]]=visited[x]+1

  for i in range(len(visited)):
    result.append(visited[i]-visited[num])
    if visited[i]-visited[num]==k:
      print(i)

  if k not in result:
    print(-1)

bfs(x)
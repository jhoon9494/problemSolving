# 숨바꼭질2
from collections import deque
n,k=map(int,input().split())

cnt=0
def BFS(start):
  visited=[0]*(10**5+1)
  visited[start]=1
  global cnt
  if start==k:
    cnt=1
    return visited[k]-1
  q=deque()
  q.append(start)
  
  while q:
    x=q.popleft()
    for nx in (x-1, x+1, 2*x):
      if 0<=nx<10**5+1:
        # 방문한 적이 없을 경우
        if visited[nx]==0:
          visited[nx]=visited[x]+1
          q.append(nx)
          if nx==k:
            cnt+=1
        # 방문한 적이 있을 경우
        elif visited[nx]!=0:
          if visited[nx]==visited[x]+1:
            if nx==k:
              cnt+=1
            else:
              # x+1일 때와 2*x일 때의 값이 같더라도 1가지만 고려하는 것이 아니라 모든 경우를 고려해야 함.
              # ex) 1+1=2, 2*1=2 이므로 1에서 2로 가는 경우의 수는 2가지.
              q.append(nx)
            
  return visited[k]-1

print(BFS(n))
print(cnt)
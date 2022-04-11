# 트리의 지름
import sys
import heapq
input=sys.stdin.readline

v=int(input())
INF=1e9
graph=[[] for _ in range(v+1)]
for _ in range(v):
  tree=list(map(int,input().split()))
  for i in range(1,len(tree)):
    if i%2!=0 and tree[i]!=-1:
      graph[tree[0]].append((tree[i],tree[i+1]))
    elif tree[i]==-1:
      break


def dijkstra(start):
  distance=[INF]*(v+1)
  q=[]
  heapq.heappush(q,(start,0))
  distance[start]=0
  while q:
    now,dist=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(i[0],cost))
  return max(distance[1:v+1]), distance.index(max(distance[1:v+1]))

max_index=dijkstra(1)[1]
result=dijkstra(max_index)[0]
print(result)
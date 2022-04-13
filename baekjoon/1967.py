# 트리의 지름
import heapq, sys
input=sys.stdin.readline
INF=1e9
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b,c=list(map(int,input().split()))
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start):
  distance=[INF]*(n+1)
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if distance[i[0]]>cost:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
  # max_index: 루트(1)에서부터 가장 먼(가중치가 가장 큰)거리에 있는 노드의 값
  max_index=distance.index(max(distance[1:n+1]))
  return (max_index, max(distance[1:n+1]))

max_index=dijkstra(1)[0]
# 루트(1)에서부터 가장 먼 거리에 있는 노드를 다시 다익스트라 함수에 넣으면 트리의 지름을 구할 수 있음.
print(dijkstra(max_index)[1])
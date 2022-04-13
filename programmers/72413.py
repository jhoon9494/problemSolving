# 합승 택시 요금
import heapq
n=7
s=3
a=4
b=1
fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
def solution(n, s, a, b, fares):
  graph=[[] for _ in range(n+1)]
  for i in fares:
      graph[i[0]].append((i[1],i[2]))
      graph[i[1]].append((i[0],i[2]))
  INF=1e9
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
    return distance[1:n+1]
  
  start=dijkstra(s)
  result=[]
  for i in range(len(start)):
    if start[i]!=INF:
      temp=dijkstra(i+1)
      result.append(start[i]+temp[a-1]+temp[b-1])
  return min(result)

print(solution(n, s, a, b, fares))
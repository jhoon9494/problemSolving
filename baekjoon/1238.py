# 파티
from heapq import heappush, heappop

def dijkstra(start, list):
  visited = [INF for _ in range(n + 1)]
  visited[start] = 0
  q = []
  for item in list[start]:
    # 해당 마을의 소요시간, 마을, 해당 마을 직전까지 오는데 걸린 시간
    heappush(q, (item[0], item[1], visited[start]))

  while q:
    t, end, prevT = heappop(q)

    if visited[end] > t + prevT:
      visited[end] = t + prevT
      for item in list[end]:
        heappush(q, (item[0], item[1], visited[end]))
  
  return visited

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverseGraph = [[] for _ in range(n + 1)]
INF = 1e9
for _ in range(m):
  start, end, t = map(int, input().split())
  heappush(graph[start], (t, end))
  heappush(reverseGraph[end], (t, start))

normal = dijkstra(x, graph)
reverse = dijkstra(x, reverseGraph)

answer = -1
for i in range(1, n + 1):
  answer = max(answer, normal[i]+reverse[i])
  
print(answer)
  

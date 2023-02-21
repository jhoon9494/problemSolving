# 택배 배송
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
  cost[start] = 0
  q = []
  heappush(q,(cost[start], start))

  while q:
    d, num = heappop(q)
    for barn in graph[num]:
      # barn[0] = 여물 비용
      # barn[1] = 헛간 위치
      if cost[barn[1]] > barn[0] + d:
        cost[barn[1]] = barn[0] + d
        heappush(q,(cost[barn[1]], barn[1]))

n, m = map(int, input().split())
cost = [1e9 for _ in range(n + 1)]
graph = [[]] + [[] for _ in range(n)]
for i in range(m):
  a, b, c = map(int, input().split())
  heappush(graph[a], (c, b)) 
  heappush(graph[b], (c, a))

dijkstra(1)
print(cost[n])
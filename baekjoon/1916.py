# 최소비용 구하기
import sys
import heapq

input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
for _ in range(m):
  bus=list(map(int,input().split()))
  graph[bus[0]].append((bus[1],bus[2]))
start,end=map(int,input().split())
# 최단거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

def dijkstra(start):
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

dijkstra(start)
print(distance[end])


# DFS 풀이(시간초과, 다익스트라 알고리즘을 이용해서 풀이해야 함)
# cost=0
# def DFS(first):
#   global cost
#   if first==end:
#     return result.append(cost)
#   for i in graph[first]:
#     if not visited[i[0]]:
#       visited[i[0]]=True
#       if i[0]==end:
#         cost+=i[1]
#         DFS(i[0])
#       else:
#         cost+=i[1]
#         DFS(i[0])
#       visited[i[0]]=False
#       cost-=i[1]

# visited=[False]*(n+1)
# result=[]
# visited[start]=True
# DFS(start)
# print(min(result))
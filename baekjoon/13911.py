# 집 구하기
import sys
import heapq
input = sys.stdin.readline
v,e = map(int,input().split())
# 맥도날드와 스타벅스에 각각 1개씩 더미노드를 추가하기 위해서 그래프 범위를 v+3로 설정
# (v = 8인 경우, 0 ~ 10번 노드이며 0번은 사용하지 않음)
# 맥도날드 더미노드에서 어떤 집까지의 거리는 그 집에서 맥도날드까지 갈 수 있는 최소 거리를 뜻함
graph=[[]for _ in range(v+3)]
INF = 1e9

for i in range(e):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

M,x = map(int,input().split())
mac = list(map(int,input().split()))
for i in mac:
  # v+1은 맥도날드의 더미노드 위치
  graph[v+1].append([i,0])
  graph[i].append([v+1,0])

S,y = map(int,input().split())
star = list(map(int,input().split()))
for i in star:
  # v+2는 스타벅스의 더미노드 위치
  graph[v+2].append([i,0])
  graph[i].append([v+2,0])

def dijkstra(start):
  global v
  distance=[INF]*(v+3)
  q=[]

  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      if i[0]==v+1 or i[0]==v+2:
        continue
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

  return distance[1:v+3]


# 맥도날드 더미노드에서 출발
macStart = dijkstra(v+1)
# 스타벅스 더미노드에서 출발
starStart = dijkstra(v+2)
min=INF
for i in range(len(macStart)):
  if macStart[i]>0 and starStart[i]>0 and macStart[i]<=x and starStart[i]<=y:
    sum=macStart[i]+starStart[i]
    if min > sum:
      min = sum
  else:
    continue

if min==INF:
  print(-1)
else:
  print(min)

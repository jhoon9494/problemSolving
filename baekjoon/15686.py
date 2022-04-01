# 치킨 배달
import sys
from itertools import combinations
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))

chicken=[(x, y) for x in range(n) for y in range(n) if graph[y][x]==2]
house=[(x, y) for x in range(n) for y in range(n) if graph[y][x]==1]
selected=list(combinations(chicken, m))

def distance():
  # 조합된 모든 경우의 수 중에서 최솟값을 찾기 위해 리스트 생성 
  result=[0]*len(selected)
  # 전체 치킨집 중 m개를 조합하여 모든 경우에 대해 반복문 실행
  for i in range(len(selected)):
    for j in house:
      dis=[0]*m
      r1=j[0]
      c1=j[1]
      # 1개의 집에서(r1,c1) m개의 치킨집 좌표까지의(r2,c2) 거리를 계산한 후 dis리스트에 저장
      for k in range(m):
        r2=selected[i][k][0]
        c2=selected[i][k][1]
        dis[k]=abs(r1-r2)+abs(c1-c2)
      # 1개의 집에서 m개의 치킨집까지 거리 중 가장 작은 값을 현재 조합의 결과(result리스트)에 반영
      # 현재 조합 중에서 좌표 내의 모든 집에 대해 계산하기 위해 min(dis) 값을 누적시킴
      result[i]+=min(dis)
  # 계산된 모든 결과중 최솟값을 출력
  return min(result)

print(distance())
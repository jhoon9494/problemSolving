# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
graph=[[]for _ in range(n+1)]
result=[0]*(n+1)

for _ in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph, start):
  for i in graph[start]:
    del graph[i][graph[i].index(start)]
    dfs(graph,i)

dfs(graph,1)

for i in range(1,len(graph)):
  for j in graph[i]:
    result[j]=i
for i in result:
  if i !=0:
    print(i)
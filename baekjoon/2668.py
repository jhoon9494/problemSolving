# 숫자 고르기

def dfs(start, now):
  if visited[now] != 0:
    if start == now:
      answer.append(start)
      return
    return

  visited[now] = 1
  dfs(start, graph[now])
    

N = int(input())
graph = [0 for _ in range(N + 1)]
answer = []

for i in range(1, N + 1):
  graph[i] = int(input())

for i in range(1, N + 1):
  visited = [0 for _ in range(N + 1)]
  dfs(i, i)
  
print(len(answer))
for i in sorted(answer):
  print(i)
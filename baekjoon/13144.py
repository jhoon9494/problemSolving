# List of Unique Numbers

n = int(input())
sequence = list(map(int, input().split()))
visited = [0] * 100001
answer = 0
end = 0

for i in range(n):  
  start = i
  

  while end < n:
    if visited[sequence[end]]:
      break
    visited[sequence[end]] = 1
    end += 1
  
  answer += (end-start)
  visited[sequence[start]] = 0

print(answer)

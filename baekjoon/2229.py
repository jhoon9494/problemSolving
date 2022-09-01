# 조 짜기
n = int(input())
students = list(map(int,input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n + 1):
  for j in range(i, 0, -1):
    max_score = max(students[j-1:i])
    min_score = min(students[j-1:i])

    dp[i] = max(dp[i], dp[j-1] + (max_score - min_score))

print(dp[n])
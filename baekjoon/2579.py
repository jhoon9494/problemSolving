# 계단 오르기
n = int(input())
score = [0 for _ in range(300)]

for i in range(n):
  score[i] = int(input())

dp = [0 for _ in range(300)]
# 첫번째 계단은 반드시 밟을 필요 없고, 마지막 계단만 반드시 밟으면 됨
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0], score[1])+ score[2]

def get_score(f):
  if f < 3:
    return dp[f]

  if dp[f] != 0:
    return dp[f]

  for i in range(3,f+1):
    dp[i] = max(get_score(i-2),get_score(i-3)+score[i-1]) + score[i]

get_score(n-1)
print(dp[n-1])

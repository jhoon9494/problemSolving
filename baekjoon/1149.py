# RGB거리
import sys
ss=sys.stdin.readline

n=int(ss())
house=[]
for i in range(n):
  house.append(list(map(int, ss().split())))

dp=[[0]*3 for _ in range(n)]

for i in range(n):
  if i==0:
    dp[i][0]=house[i][0]
    dp[i][1]=house[i][1]
    dp[i][2]=house[i][2]
  else:
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+house[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+house[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+house[i][2]

print(min(dp[n-1]))
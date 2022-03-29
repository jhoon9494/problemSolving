# LCS
f=input()
s=input()

dp=[[0]*(len(f)+1) for _ in range(len(s)+1)]

for i in range(1,len(s)+1):
  for j in range(1,len(f)+1):
    if s[i-1]==f[j-1]:
      dp[i][j]=1+dp[i-1][j-1]
    else:
      dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[len(s)][len(f)])
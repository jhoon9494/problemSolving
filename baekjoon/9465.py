# 스티커
import sys
ss=sys.stdin.readline

t=int(ss())

while t>0:
  n=int(ss())
  sticker=[]
  for i in range(2):
    sticker.append(list(map(int, ss().split())))
  dp=[[0]*n for _ in range(2)]
  
  # 점화식부터 세워서 접근하기
  for i in range(n):
    if i==0:
      dp[0][i]=sticker[0][i]
      dp[1][i]=sticker[1][i]
    elif i==1:
      dp[0][i]=sticker[1][i-1]+sticker[0][i]
      dp[1][i]=sticker[0][i-1]+sticker[1][i]
    else:
      dp[0][i]=max(dp[1][i-1],dp[1][i-2])+sticker[0][i]
      dp[1][i]=max(dp[0][i-1],dp[0][i-2])+sticker[1][i]  

  print(max(max(dp[0]),max(dp[1])))
  t-=1
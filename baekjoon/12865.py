# 평범한 배낭
import sys
ss=sys.stdin.readline

n,k=map(int,ss().split())
items=[]
for i in range(n):
  items.append(list(map(int,ss().split())))
# 배낭의 무게를 1~K까지의, 물건의 개수를 n만큼 지정하여 2차원 배열 생성
# 계산을 편하게 하기위해 인덱스 0번은 사용 X
dp=[[0]*(k+1) for _ in range(n)]

for i in range(n):
  for j in range(1,k+1):
    # 가방의 무게(j)가 물건의 무게보다 크거나 같을 경우 물건의 가치를 dp배열에 저장
    if j>=items[i][0]:
      # items[i][1]: 현재 물건의 가치
      # dp[i-1][j-items[i][0]]: 현재 물건을 넣고 남은 무게 중 채울 수 있는 물건의 가치
      dp[i][j]=max(items[i][1]+dp[i-1][j-items[i][0]],dp[i-1][j])
    else:
      # 가방의 무게(j)가 물건의 무게보다 작을 경우 이전 dp값을 저장
      dp[i][j]=dp[i-1][j]
  
print(dp[n-1][k])
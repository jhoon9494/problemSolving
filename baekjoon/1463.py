# 1로 만들기
# top-down방식
n=int(input())

# 최소값(min)비교를 위해 dp리스트 초기값으로 매우 큰 값인 1e9를 지정 
dp=[1e9]*(n+1)
# 입력받은 정수 n은 연산을 실행하지 않았기 때문에 0으로 지정
dp[n]=0

# i=n부터 2까지 내려가며 각각 연산된 횟수 중 최솟값을 리스트의 값으로 지정
for i in range(n,1,-1):
  if i%3==0:
    dp[i//3]=min(dp[i//3],dp[i]+1)
  if i%2==0:
    dp[i//2]=min(dp[i//2],dp[i]+1)
  if i>0:
    dp[i-1]=min(dp[i-1],dp[i]+1)

# 정수 n부터 1까지 연산된 횟수를 출력
print(dp[1])
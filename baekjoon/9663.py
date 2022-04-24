# N-Queen

n=int(input())
row=[-1 for _ in range(n)]
cnt=0

def place(start):
  for i in range(start):
    # row[start]==row[i] : 같은 열에 퀸이 존재할 경우 False
    # abs(row[start]-row[i])==abs(start-i) : 대각선에 퀸이 존재할 경우 False
    if row[start]==row[i] or abs(row[start]-row[i])==abs(start-i):
      return False
  # 퀸의 공격을 받지 않는 장소일 경우 true를 반환하여 다음 퀸을 배치하도록 이동
  return True 

def dfs(start):
  global cnt
  if start==n:
    cnt+=1
    return 
  else:
    for i in range(n):
      # (row[start], start)좌표에 퀸을 둠
      row[start]=i
      if place(start):
        dfs(start+1)
    

dfs(0)
print(cnt)
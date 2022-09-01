# 회의실 배정

n = int(input())
time = [0 for _ in range(n)]

for i in range(n):
  time[i] = list(map(int,input().split()))

# 회의가 끝나는 시간을 기준으로 정렬하되, 끝나는 시간이 같다면 시작시간으로 정렬
sorted_time = sorted(time, key = lambda x : (x[1],x[0])) 

result = []
for i in range(n):
  if i == 0:
    result.append(sorted_time[i])
    continue
  
  prev = result[-1]
  curr = sorted_time[i]

  if prev[1] <= curr[0]:
    result.append(sorted_time[i])
    
print(len(result))


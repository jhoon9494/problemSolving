# IF문 좀 대신 써줘
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
std = []

for i in range(n):
  name, limit = input().split()

  if i == 0:
    std.append([name, 0])
  
  # 이미 동일한 전투력이 존재하는 경우 std 배열에서 생략
  if std[-1][1] == limit:
    continue 

  std.append([name, limit])

for _ in range(m):
  player = int(input())
  start = 0
  end = len(std) - 1

  while True:
    center = (start + end) // 2
    limitValue = int(std[center][1])
    
    if limitValue == player:
      print(std[center][0])
      break
    else:
      if end - start == 1:
        print(std[end][0])
        break
      elif player > limitValue:
        start = center
      else:
        end = center
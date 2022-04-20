# 용액
import sys
input=sys.stdin.readline

n=int(input())
solution=list(map(int,input().split()))
min_sum=1e9*2
min_value=(0,0)

start=0
end=n-1

for i in range(n):
  sum=solution[start]+solution[end]

  # 최소 값 구하는 조건
  if abs(min_sum)>abs(sum):
    min_sum=sum
    min_value=(solution[start],solution[end])
  
  # 포인터 이동
  # 정렬이 되어 있기 때문에 합계가 양수, 음수 조건으로 포인터를 이동
  if sum>0:
    end-=1
  elif sum<0:
    start+=1
  else:
    break
  
  # 포인터가 겹칠 때 
  if end==start:
    break;

print(min_value[0],min_value[1])
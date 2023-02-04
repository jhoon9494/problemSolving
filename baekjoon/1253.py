# 좋다
import sys
input = sys.stdin.readline    
N = int(input())
list = sorted(list(map(int,input().split())))
count = 0


for i in range(N): 
  currentNumber = list[i]
  newList = list[0:i] + list[i+1:]
  startIndex = 0
  endIndex = N - 2

  while(startIndex < endIndex):
    sum = newList[startIndex] + newList[endIndex]
    if sum > currentNumber: 
      endIndex -= 1
      continue
    elif sum == currentNumber: 
      count += 1
      break
    else:
      startIndex += 1

print(count)
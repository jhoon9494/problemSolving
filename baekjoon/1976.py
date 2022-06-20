# 여행 가자
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
group = [i for i in range(n)]

def getGroup(city):
  if(group[city] == city):
    return city
  group[city] = getGroup(group[city])
  return group[city]

for i in range(n):
  cityList = list(map(int, input().split()))
  for city in range(len(cityList)):
    if(cityList[city] == 1):
      groupA = getGroup(i)
      groupB = getGroup(city)
      if(groupA > groupB):
        group[groupA] = groupB
      else:
        group[groupB] = groupA

plan = list(map(int, input().split()))


for i in range(len(plan)):
  if i == 0:
    firstCity = getGroup(plan[i] - 1)
    if i == len(plan) - 1:
      print("YES")
  elif i == len(plan) - 1 and firstCity == getGroup(plan[i] - 1):
    print("YES")
  else:
    if firstCity != getGroup(plan[i] - 1):
      print("NO")
      break
  
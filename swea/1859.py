# 백만 장자 프로젝트

t = int(input())
count = 0

for i in range(2 * t):
  if i % 2 == 0:
    n = int(input())
    count += 1
    continue
  else:
    priceList = list(map(int, input().split()))
    maxPrice = priceList[-1]
    totalPrice = 0
  
  for j in range(len(priceList)-2, -1, -1):
    if maxPrice > priceList[j]:
      totalPrice += maxPrice - priceList[j]
    else:
      maxPrice = priceList[j]

     
  print(f'#{count} {totalPrice}')

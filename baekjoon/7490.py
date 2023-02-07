# 0 만들기

def calc(count, text, num):
  if count == N:
    sum = text.replace(" ","")
    if eval(sum) == 0:
      print(text)
    return
  
  count+=1
  calc(count, text+" "+str(num+1), num+1)
  calc(count, text+"+"+str(num+1), num+1)
  calc(count, text+"-"+str(num+1), num+1)

case = int(input())
for i in range(case):
  N = int(input())
  if i != 0:
    print()
  calc(1, "1", 1)


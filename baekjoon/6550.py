# 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.
import sys
def check_statement(s,t):
  i=0
  j=0
  temp=[]

  while True:
    if i<len(s) and j<len(t):
      if s[i]==t[j]:
        temp.append(t[j])
        i+=1
        j+=1
      else:
          j+=1
    else:
      break

  if s==temp:
    print("Yes")
  else:
    print("No")

while True:
  a=sys.stdin.readline().strip()
  text=a.split()
  if not a:
    break
  
  s=list(text[0])
  t=list(text[1])
  check_statement(s,t)



s=list(input())
cnt=0
cnt1=0
result=[]

for i in range(len(s)):
  if s[i]=="X":
    cnt+=1

    if cnt==2:
      for j in range(cnt):
        s[i-j]="B"
      cnt=0

for i in range(len(s)):
  if s[i]=="B":
    cnt1+=1
    if cnt1==4:
      for j in range(cnt1):
        s[i-j]="A"
      cnt1=0
  else:
    cnt1=0    

if "X" in s:
  print(-1)
else:
  print("".join(s))
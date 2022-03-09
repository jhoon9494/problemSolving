s=list(map(int,input()))
arr0=[]
arr1=[]
cnt0=0
cnt1=0

for i in range(len(s)):
  if s[i]==0:
    cnt0+=1
    if i == int(len(s)-1) and s[len(s)-1]==0:
        arr0.append(cnt0)
    if cnt1!=0: 
      arr1.append(cnt1)
      cnt1=0
  else:
    cnt1+=1
    if i == int(len(s)-1) and s[len(s)-1]==1:
        arr1.append(cnt1)
    if cnt0!=0:
      arr0.append(cnt0)
      cnt0=0
     
if len(arr0)>=len(arr1):
  print(len(arr1))
else:
  if len(arr0)==0:
    print(len(arr0))
  else:
    if len(arr1)==0:
      print(len(arr1))
    else:
      print(len(arr0))
  


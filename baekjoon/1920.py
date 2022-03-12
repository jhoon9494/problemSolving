import sys
ss=sys.stdin.readline

N=int(ss())
A=list(map(int,ss().split()))
A.sort()
M=int(ss())
nums=list(map(int,ss().split()))



def found_number(target):
  low=0
  high=N-1

  while low<=high:
    mid=(low+high)//2
    mid_num=A[mid]
    if target==mid_num:
      return True
    elif target>mid_num:
      low=mid+1
    else:
      high=mid-1
      


for i in range(M):
  if found_number(nums[i]):
    print("1")
  else:
    print("0")
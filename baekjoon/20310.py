# 타노스
import sys
input = sys.stdin.readline
s = list(input().strip())

zeroCount = 0
oneCount = 0

for num in s:
  if num == "0":
    zeroCount += 1
  else:
    oneCount += 1

zeroCount //= 2
oneCount //= 2
zero = len(s) - 1
one = 0

while zeroCount or oneCount:
  if zeroCount and s[zero] == "0":
    zeroCount -= 1
    s[zero] = ''
  
  if oneCount and s[one] == "1":
    oneCount -= 1
    s[one] = ''
  
  zero -= 1
  one += 1

print(''.join(s))
import sys
input=sys.stdin.readline
case=0

def carcul(L,P,V,case):
  if L>= V%((V//P)*P):
    result=(V//P)*L + V%((V//P)*P)
    print( f"Case {case}: {result}")
  else:
    result=(V//P)*L + L
    print( f"Case {case}: {result}")

while True:
  L,P,V=(map(int,input().split()))
  if L<=1 or P<=L or P>=V: 
    break
  case+=1
  carcul(L,P,V,case)
  

# f formatting 
# javascript의 템플릿 리터럴(백틱)과 유사한 시스템
# 이 때 주의해야할 것은 f formatting 문법을 사용하기 위해서는 print( 이후에 f로 시작해야합니다.
# print( "hello {wld} {name}")으로 작성 X
# print( f"hello {wld} {name}")으로 작성하셔야합니다, f 사용에 주의하세요.
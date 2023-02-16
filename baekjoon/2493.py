# 탑

def lazer(t, i):
  # 스택이 빈 경우 본인이 가장 높은 탑이므로 수신받을 탑이 없기때문에 0을 반환
  if not stack:
    stack.append([t,i])
    return 0

  # 스택의 제일 마지막에 있는 값과 탑의 값을 비교하여 스택의 값이 큰 경우 현재 탑의 값과 탑의 위치를 스택에 삽입
  if stack[-1][0] > t:
    resultIndex = stack[-1][1]
    stack.append([t, i])
    return resultIndex

  # 스택의 값이 탑의 값보다 작은 경우 현재 스택의 마지막 값을 빼고 재귀를 통해 탑의 값을 계속해서 비교
  else:
    stack.pop()
    return lazer(t, i)


n = int(input())
tower = list(map(int,input().split()))
stack = []
answer = []

for i in range(n):
  answer.append(lazer(tower[i], i + 1))

print(" ".join(map(str,answer)))

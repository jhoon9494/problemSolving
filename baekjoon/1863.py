# 스카이라인 쉬운거

n = int(input())
# x가 최대 100만 y가 최대 50만을 입력받으므로 맵을 그리는데만 5천억번을 반복해야해서 무조건 시간초과 발생함
# 보통 1억번 반복에 1초임
# 그래프를 직접 그려서 대입하는 문제가 아님
# n을 최대 5만번 받으므로 입력받는 값을 이용해서 문제를 풀이해야 함

stack = []
count = 0
for i in range(n):
  x, y = map(int, input().split())
  # 스택이 비었을 경우 높이를 삽입
  # 이 때 높이가 0일 경우엔 건물이 없는 것이므로 삽입 X
  if not stack:
    if y != 0:
      stack.append(y)
  
  # 스택의 마지막 높이보다 현재 건물의 높이가 큰 경우, 현재 건물의 높이를 스택에 삽입
  elif stack[-1] < y:
    stack.append(y)
  
  # 스택의 마지막 높이가 더 높은 경우  
  elif stack[-1] > y:
    # 이 때, 스택에 남은 건물이 있다면 각 건물 높이와 현재 건물의 높이를 비교하여 추가적으로 건물 개수를 세어준다.
    while stack:
      if stack[-1] > y:
        stack.pop()
        count += 1
      elif stack[-1] < y:
        stack.append(y)
      else:
        break

    if not stack and y != 0:
      stack.append(y)


count += len(stack)
print(count)

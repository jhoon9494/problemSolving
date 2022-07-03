# 두 용액

# 주어진 용액들 중 두가지를 혼합하여 0에 가장 가까운 용액을 만들어내는 두가지 용액을 출력
# 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우 그 중 아무거나 한가지를 출력
import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))
# 투포인터 사용을 위해 정렬
solution.sort()

start = 0
end = n-1
sum = 1e9 * 2
result = (0, 0)

while True: 
  if start == end:
    break

  solution_sum = solution[start] + solution[end]

  if abs(sum) > abs(solution_sum):
    sum = solution_sum
    result = (solution[start], solution[end])

  if solution_sum < 0:
    start += 1
  elif solution_sum > 0:
    end -= 1
  # 합계가 0일 경우 무조건 최소값이기 때문에 더 찾을 필요 없이 반복문을 종료시킴
  else:
    break

print(result[0], result[1])
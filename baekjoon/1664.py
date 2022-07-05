# 소수의 연속합
n = int(input())

def find_prime(n):
  # 1은 소수가 아니므로 별도 처리
  if n < 2:
    return [0]
  list = [True] * (n + 1)

  m = int(n ** 0.5)
  for i in range(2, m + 1):
    if list[i] == True:
      for j in range(2 * i, n + 1, i):
        list[j] = False
  
  return [i for i in range(2, n + 1) if list[i]== True]


prime_list = find_prime(n)
start = 0
end = 0
list_sum = prime_list[0]

# 소수의 합으로 나타낼 수 있는 경우의 수 
count = 0

while True:
  if list_sum < n:
    end += 1

    if end > len(prime_list) - 1:
      break

    list_sum += prime_list[end]

  else:
     # 소수의 합으로 n을 나타낼 수 있는 경우
    if list_sum == n:
      count += 1
    list_sum -= prime_list[start]
    start += 1

print(count)
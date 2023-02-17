# 성냥 개비
def maxStickCounter(number):
  # 그리디
  # 자릿수가 많으면 최대값이므로 2를 최대한 넣어준다. 
  maxNumber = ""
  maxCnt = number // 2
  while(True):
    rest = number - (2 * maxCnt)
    
    # 성냥이 1개 남았다면 만들 수 있는 숫자가 없으므로 count를 1빼줌
    if rest == 1:
      maxCnt -= 1

    else:
      # 성냥이 3개 남았다면 우선 3을 먼저 삽입
      if rest == 3:
        maxNumber += str(matchstick[3][-1])
      for _ in range(maxCnt):
        maxNumber += str(matchstick[2][-1])
      break
  return maxNumber


def minStickCounter(number):
  # DP
  if minNumberDp[number] != 0:
    return str(minNumberDp[number])
  
  if number > 11:
    
    if number == 17:
      # 성냥개비가 17개인 경우 10 + 7보다 11 + 6일 때 더 작은 수를 만들 수 있으므로 별도 처리해줌. 
      minNumberDp[number] = int(str(minNumberDp[11]) + "0") # dp[6]의 가장 작은 값인 0을 가져옴
    else: 
      minNumberDp[number] = int(str(minStickCounter(number - 7)) + str(minNumberDp[7]))

  return str(minNumberDp[number])



t = int(input())
# 각 인덱스에 해당하는 성냥개비 개수로 만들 수 있는 숫자 배열
matchstick = [0, 0, [1], [7], [4], [2, 3, 5], [0, 6, 9], [8]]

# 최솟값을 구하기 위한 dp 배열
minNumberDp = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20] + [0] * 89
answer = []
for case in range(t):
  n = int(input())
  answer.append([minStickCounter(n), maxStickCounter(n)])

for ans in answer:
  print(ans[0], ans[1])
  
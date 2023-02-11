# 보호 필름

# 각 열마다 연속된 알파벳의 개수가 성능검사 개수인 K개를 만족하는지 체크 
def check(list):
  for row in range(w):
    cnt = 1
    for col in range(1, d):
      if list[col][row] == list[col-1][row]:
        cnt += 1
      else: 
        cnt = 1
      if cnt >= k: # 만족할 경우 다음 열로 이동
        break
    if cnt < k: # 하나라도 만족하지 못할 경우 즉시 False 반환
      return False 
  return True # 모두 만족한다면 True 반환


def injectMedichine(currRow, count):  
  global result

  # count = 약품 바른 횟수 (재귀 횟수)
  if count >= result:
    return

  # 테스트 진행
  if check(filmList):
    if result > count:
        result = count
    return

  # 연속적으로 약품을 k번 바른다면 무조건 테스트에 통과하므로 종료시킴
  if count == k:
    if result > count:
      result = count
    return

  else :
    for r in range(currRow, d):
      for idx in range(2):
        filmList[currRow] = medicine[idx]
        injectMedichine(r + 1, count+1)
        filmList[currRow] = original[currRow] 


t = int(input())
for i in range(t):
  d, w, k = list(map(int, input().split()))
  filmList = [list(map(int, input().split())) for _ in range(d)]
  original = [film[:] for film in filmList]
  medicine = [[0] * w, [1] * w]

  # 합격 기준이 1인 경우 모든 경우에 통과함
  if k == 1:
    print(f'#{i+1} 0')
  else:
    result = 1e9
    for row in range (0, d):
      injectMedichine(row, 0)
    
    print(f'#{i+1}',result)

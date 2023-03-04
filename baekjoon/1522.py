# 문자열 교환
string = [*input()]
aCount = 0

for str in string:
  if str == "a":
    aCount += 1

answer = 1e9
slidingStart = 0
slidingEnd = aCount 

while slidingStart < len(string):
  if slidingEnd <= len(string):
    sliding = string[slidingStart: slidingEnd]
  else:
    newIndex = slidingEnd - len(string)
    sliding = string[slidingStart:] + string[: newIndex]
  count = 0

  for str in sliding:
    if str == "b":
      count += 1
  answer = min(answer, count)
  slidingStart += 1
  slidingEnd += 1

print(answer)


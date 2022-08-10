# 파일 정리
import sys
input = sys.stdin.readline

n = int(input())
extensions=dict()
for i in range(n):
  file, extension = input().split(".")
  extension = extension.rstrip()
  if extension not in extensions:
    extensions[extension] = 1
  else:
    extensions[extension] += 1

sort_keys = extensions.items()
sorted_extensions = sorted(sort_keys)
for i in sorted_extensions:
  print(i[0], i[1])
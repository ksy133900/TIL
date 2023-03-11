s = list(input())
a_cnt = s.count('a')
answer = 999999999999999
left = 0

while left < len(s):
  right = left + a_cnt
  if right > len(s):
    temp = s[left:len(s)] + s[:right-len(s)]
  else:
    temp = s[left:right]
  answer = min(answer, temp.count('b'))
  left += 1

print(answer)

## 문제
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
word = 'banana'
for i in word:
    print(chr(ord(i)-32),end=' ')

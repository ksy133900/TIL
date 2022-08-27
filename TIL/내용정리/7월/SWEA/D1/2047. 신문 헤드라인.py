# input = The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
#import sys
#sys.stdin = open("input.txt", "r")
t=input()
result=''
for i in t:
    if i=='T':
        result+=i
    elif i=='_':
        result+=i
    elif i=='.':
        result+=i
    else:
        b=ord(i)-32
        c=chr(b)
        result+=c
print(result)

#! 쉽게 하는 방법... upper()로 대문자 바꿔버리면 1줄로 컷...
print(t.upper())
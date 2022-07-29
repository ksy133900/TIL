# https://www.acmicpc.net/problem/2908
# 2908
import sys
sys.stdin = open("1_상수.txt")

a,b = map(int,input().split()) # 두 정수 a,b를 공백을 두고 입력

a = str(a)  #두 정수 a,b를 각각 문자열로 변환
b = str(b)

c = int(str(a[::-1]))   #문자열로 변환한 a,b를 슬라이싱을 이용해 거꾸로 하고, .
d = int(str(b[::-1]))   # 다시 int형으로 변환후 각 각 c와 d에 할당한다.

if c > d : #c > d면 c 출력 , 아니라면 d 출력
    print(c)
else:
    print(d)

# https://www.acmicpc.net/problem/2577
# 2577
import sys
sys.stdin = open("0_숫자의개수.txt")

a = int(input()) #줄을 바꿔가면서 입력을 받으므로 한줄마다 input()
b = int(input()) 
c = int(input())

# 17037300 = 1,7,0,3,7,3,0,0 이므로 문자열로 변환해서 count함수로 갯수를 세는 방향으로 접근

d = str(a*b*c) # str함수를 이용하여 문자열로 변환.

for i in range(10): # 0부터 9의 문자를 str(i)의 i값에 할당해야 하므로 -> range(10) 
    print(d.count(str(i))) # str에 i 값을 대입해가면서 숫자들을 count 합니다.
   
   # for ~ range 쓰지 않고 작성하면 아래와 같다. 
   # print(d.count(str('0')))                       
   # print(d.count(str('1')))
   #.....
   # print(d.count(str('8')))
   # print(d.count(str('9')))
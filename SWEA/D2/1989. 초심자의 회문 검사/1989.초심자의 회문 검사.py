# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
#import sys
#sys.stdin = open("input.txt", "r")

T=int(input())
for a in range(0,T):
    x=input()
    reversed_str = x[::-1]
    if x == x[::-1]:
        print('#%d %d'% (a+1, 1))
    else :
        print('#%d %d'% (a+1, 0))
        